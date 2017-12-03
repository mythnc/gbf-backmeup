import csv
from os.path import join
import sqlite3
from . import package_dir


db_name = 'gbf_backmeup' + '_test' + '.db'
conn = sqlite3.connect(join(package_dir, db_name))
c = conn.cursor()
c.execute('PRAGMA foreign_keys=ON')

lang_id = {'ja': 1, 'en': 2}

class Boss:
    def __init__(self):
        self.name = ""
        self.level = ""
        self.lang = ""
        self.image = ""
        self._boss_id = ""

    def save(self):
        '''Save Boss data if not exists'''
        if self.is_exists():
            self.update_image()
            return self._boss_id

        self.save_level()
        self.save_locale()
        return self._boss_id

    def is_exists(self):
        c.execute('''select b.id
                   from boss_locale b_locale
                   inner join boss b on (b.id = b_locale.boss_id and b.level = ?)
                   where name = ?''', (self.level, self.name))
        try:
            self._boss_id = c.fetchone()[0]
        except TypeError:
            return False
        return True

    def update_image(self):
        'Update boss image if self.image is not None and boss_locale.image is null'
        if self.image is None:
            return

        c.execute('''select id, image from boss_locale
                     where boss_id = ? and language_id = ?''',
                  (self._boss_id, lang_id[self.lang]))

        row = c.fetchone()
        if row[1]:
            return

        boss_locale_id = row[0]
        c.execute('update boss_locale set image = ? where id = ?',
                  (self.image, boss_locale_id))
        conn.commit()

    def save_level(self):
        c.execute('insert into boss (level) values (?)', (self.level,))
        conn.commit()
        self._boss_id = c.lastrowid

    def save_locale(self):
        c.execute('insert into boss_locale (name, image, boss_id, language_id)'\
                    'values (?, ?, ?, ?)',
                  (self.name, self.image, self._boss_id, lang_id[self.lang]))
        conn.commit()


class User:
    def __init__(self, lang):
        self.twitter = ""
        self.lang = lang
        self._user_id = ""

    def save(self):
        '''Save User data if not exists'''
        if self.is_exists():
            return self._user_id

        c.execute('insert into user (twitter, language_id) values (?, ?)',
                  (self.twitter, lang_id[self.lang]))
        conn.commit()
        self._user_id = c.lastrowid
        return self._user_id

    def is_exists(self):
        c.execute('select id from user where twitter = (?)', (self.twitter,))
        try:
            self._user_id = c.fetchone()[0]
        except TypeError:
            return False
        return True

class Battle:
    def __init__(self):
        self.room = ""
        self.message = ""
        self._timestamp = ""
        self.lang = ""

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        month_map = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12,
        }
        _, raw_month, day, time, _, year = timestamp.split(' ')
        month = month_map[raw_month]
        self._timestamp = '{}-{}-{} {}'.format(year, month, day, time)

    def save(self, boss_id, user_id):
        # assume room is unique
        c.execute('insert into battle (timestamp, message, room, boss_id, user_id)'\
                    'values (?, ?, ?, ?, ?)',
                  (self._timestamp, self.message, self.room, boss_id, user_id))
        conn.commit()


def create_tables():
    c.execute('''create table if not exists boss (
                  id integer primary key,
                  level integer not null
                 )''')
    c.execute('''create table if not exists language (
                  id integer primary key,
                  name text not null
                 )''')
    c.execute('''create table if not exists boss_locale (
                  id integer primary key,
                  name text not null,
                  image text,
                  boss_id integer,
                  language_id integer,
                  foreign key (boss_id) references boss (id),
                  foreign key (language_id) references language (id)
                 )''')
    c.execute('''create table if not exists user (
                  id integer primary key,
                  twitter text not null,
                  language_id integer,
                  foreign key (language_id) references language (id)
                 )''')
    c.execute('''create table if not exists battle (
                  id integer primary key,
                  timestamp text not null,
                  message text,
                  room text not null,
                  boss_id integer,
                  user_id integer,
                  foreign key (boss_id) references boss (id),
                  foreign key (user_id) references user (id)
                 )''')
    conn.commit()


def insert_predefined_data():
    c.execute("""insert into language (name) values
                  ('ja'),
                  ('en')""")
    csv_file = 'boss_locale.csv'
    with open(join(package_dir, csv_file)) as f:
        reader = csv.DictReader(f)
        for row in reader:
            c.execute('''insert into boss (level) values (?)''', (row['level'],))
            boss_id = c.lastrowid
            c.execute('''insert into boss_locale (name, boss_id, language_id)
                          values (?, ?, ?)''', (row['ja_name'], boss_id, 1))
            c.execute('''insert into boss_locale (name, boss_id, language_id)
                          values (?, ?, ?)''', (row['en_name'], boss_id, 2))
    conn.commit()


if __name__ == '__main__':
    create_tables()
    insert_predefined_data()
