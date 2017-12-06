from datetime import datetime
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


def find(boss_name='', boss_level='', timestamp=''):
    logger.info('start search battles')
    logger.info('boss name - %s', boss_name)
    logger.info('boss level - %s', boss_level)
    if not timestamp:
        timestamp = datetime.utcnow()
    try:
        since_id = 0
        while True:
            c = models.search_battles(boss_name, boss_level, timestamp,
                                      since_id)
            rooms = c.fetchall()
            if not rooms:
                print('waiting...\n')
                time.sleep(1)
                continue

            timestamp = rooms[-1][3]
            since_id = rooms[-1][0]
            logger.debug(timestamp)
            logger.debug(since_id)
            for i, row in enumerate(rooms):
                if i % 5 == 0:
                    print()
                    time.sleep(5)
                print('{} {}'.format(row[1], row[2]))
    except KeyboardInterrupt:
        logger.info('end search battles')
        return
