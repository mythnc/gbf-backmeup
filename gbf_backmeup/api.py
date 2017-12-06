import logging
import time
from . import models, crawler, wipe_out


logger = logging.getLogger(__name__)


def model():
    logger.info('start create table schema')
    models.create_tables()
    logger.info('end create table schema')

    logger.info('start insert predefined data')
    models.insert_predefined_data()
    logger.info('end insert predefined data')


def crawl():
    logger.info('start crawl battle data')
    try:
        crawler.start()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info('end crawl battle data')


def wipeout():
    logger.info('start wipe out')
    wipe_out.start()
    logger.info('end wipe out')


def find(boss_name='', boss_level='', timestamp="datetime('now')"):
    logger.info('start search battles')
    try:
        since_id = 0
        while True:
            c = models.search_battles(boss_name, boss_level, timestamp,
                                      since_id)
            rooms = c.fetchall()
            if not rooms:
                time.sleep(1)
                continue

            timestamp = rooms[-1][3]
            since_id = rooms[-1][0]
            print(timestamp)
            print(since_id)
            for i, row in enumerate(rooms):
                if i % 5 == 0:
                    print()
                    time.sleep(2)
                print('{} {}'.format(row[1], row[2]))
    except KeyboardInterrupt:
        logger.info('end search battles')
        return
