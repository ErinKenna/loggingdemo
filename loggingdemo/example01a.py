import logging
import os
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(message)s')
log = logging.getLogger(os.path.basename(__file__))

log.info('a message')
log.info('done')

