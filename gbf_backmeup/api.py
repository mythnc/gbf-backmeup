import logging
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
