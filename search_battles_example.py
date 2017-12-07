from datetime import datetime
import time
from gbf_backmeup.models import search_battles


def find(boss_name='', boss_level=''):
    timestamp = datetime.utcnow()
    since_id = 0
    try:
        while True:
            rooms = search_battles(boss_name, boss_level, timestamp, since_id)
            if not rooms:
                print('waiting...\n')
                time.sleep(2.5)
                continue

            timestamp = rooms[-1][3]
            since_id = rooms[-1][0]
            for i, row in enumerate(rooms):
                if i % 5 == 0:
                    print()
                    time.sleep(5)
                print('{} {}'.format(row[1], row[2]))
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    find('Luminiera Omega', 75)
