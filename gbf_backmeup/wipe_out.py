import logging
from .constants import twitter_api as api


logger = logging.getLogger(__name__)


def delete_backup_messages():
    logger.info('start delete backup messages')
    screen_name = find_screen_name()
    r = api.request('statuses/user_timeline',
                    {'screen_name': screen_name,
                     'trim_user': True,
                     'count': 200})
    for i, tweet in enumerate(r):
        source = tweet['source']
        if source != ('<a href="http://granbluefantasy.jp/" '
                      'rel="nofollow">グランブルー ファンタジー</a>'):
            continue

        try:
            result = api.request('statuses/destroy/:{}'.format(tweet['id']),
                                 {'trim_user': True})
            for data in result:
                logger.info("%s %s", i+1, data['id'])
        except Exception as e:
            logger.error(e)
            return
    logger.info('end delete backup messages')


def find_screen_name():
    r = api.request('account/verify_credentials',
                    {'include_entities': False, 'skip_status': True})
    for data in r:
        return data['screen_name']


def start():
    delete_backup_messages()


if __name__ == '__main__':
    start()
