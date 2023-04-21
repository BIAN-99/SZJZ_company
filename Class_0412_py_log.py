from datetime import datetime
import logging

# datetime.now().replace(microsecond=0)中的replace方法可以截取毫秒
s = 'log ' + str(datetime.now().replace(microsecond=0)).replace(':', "").replace('-', "")

logging.basicConfig(level=logging.DEBUG, filename=s)


def run():
    logging.debug('this is dug log')
    logging.info('this is info log')
    logging.warning('this is warning log')
    logging.error('this is error log')
    logging.critical('this is critical log')


run()
