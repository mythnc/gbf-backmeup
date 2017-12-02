import logging
import os
from os.path import join
import re
import requests
from TwitterAPI import TwitterAPI
from . import consumer_key, consumer_secret, token, token_secret
from . import images_dir
from .models import Boss, User, Battle


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

api = TwitterAPI(consumer_key, consumer_secret, token, token_secret)


def parse_text(text, lang):
    if lang == 'en':
        pattern = r'''(?P<message>(?:.*\n)*.*?)?       # message if any
                      (?P<room>\w{8})[ ]:Battle[ ]ID\n # room name
                      I[ ]need[ ]backup!\n
                      Lvl[ ](?P<level>\d+)[ ]          # level
                      (?P<boss>.*)                     # boss name
                      (?:\nhttps.*)?                   # image url if any'''
    elif lang == 'ja':
        pattern = r'''(?P<message>(?:.*\n)*.*?)?  # message if any
                      (?P<room>\w{8})[ ]:参戦ID\n # room name
                      参加者募集！\n
                      Lv(?P<level>\d+)[ ]         # level
                      (?P<boss>.*)                # boss name
                      (?:\nhttps.*)?              # image url if any'''
    else:
        logger.error('no matched lang:')
        logger.error(lang)
        logger.error(text)
        return

    p = re.compile(pattern, re.VERBOSE)
    m = p.match(text)

    if m is None:
        logger.error('no matched text:')
        logger.error(text)
        return

    boss = Boss()
    boss.name = m.group('boss')
    boss.level = m.group('level')

    battle = Battle()
    battle.message = m.group('message')
    battle.room = m.group('room')
    return boss, battle


def save_image(url):
    file_name = url.split('/')[-1]
    path = join(images_dir, file_name)
    if os.path.exists(path):
        logger.debug('image exists')
        return file_name

    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
    logger.debug('image saved')
    return file_name


def start():
    jp_match = [':参戦ID', '参加者募集！']
    en_match = ['I need backup!', ':Battle ID']
    r = api.request('statuses/filter',
                    {'track': '{j[0]} {j[1]},{e[0]} {e[1]}'.format(j=jp_match,
                                                                   e=en_match)})
    for item in r:
        source = item['source']
        if source != ('<a href="http://granbluefantasy.jp/" '
                      'rel="nofollow">グランブルー ファンタジー</a>'):
            continue

        try:
            image_url = item['entities']['media'][0]['media_url']
            image = save_image(image_url)
        except KeyError:
            image = None
        text = item['text']
        if jp_match[0] in text:
            lang = 'ja'
        elif en_match[0] in text:
            lang = 'en'
        boss, battle = parse_text(text, lang)
        boss.image = image
        boss.lang = lang
        battle.date = item['created_at']

        user = User(lang)
        user.twitter = item['user']['screen_name']

        boss_id = boss.save()
        user_id = user.save()
        battle.save(boss_id, user_id)
        logger.info('data saved\n')
