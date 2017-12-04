import logging
from urllib3.exceptions import ConnectTimeoutError
from .constants import twitter_api as api
from .models import delete_battles


logger = logging.getLogger(__name__)


def delete_backup_messages():
    logger.info('start delete backup messages')
    screen_name = find_screen_name()
    r = api.request('statuses/user_timeline',
                    {'screen_name': screen_name,
                     'trim_user': True,
                     'count': 200})
    count = 0
    for tweet in r:
        source = tweet['source']
        if source != ('<a href="http://granbluefantasy.jp/" '
                      'rel="nofollow">グランブルー ファンタジー</a>'):
            continue
        count += 1

        try:
            result = api.request('statuses/destroy/:{}'.format(tweet['id']),
                                 {'trim_user': True})
            for data in result:
                logger.info("%s %s", count, data['id'])
        except ConnectTimeoutError:
            logger.error('ConnectTimeoutError. Try again later.')
            return
    logger.info('deleted %d tweets', count)
    logger.info('end delete backup messages')


def find_screen_name():
    r = api.request('account/verify_credentials',
                    {'include_entities': False, 'skip_status': True})
    for data in r:
        return data['screen_name']


def start():
    delete_backup_messages()
    logger.info('start delete battle rooms')
    n = delete_battles()
    logger.info('%d rooms deleted', n)
    logger.info('end delete battle rooms')


if __name__ == '__main__':
    start()
