""" Refactor the divide method into a separate module.
"""

import itertools
import logging.config
import os
import pathlib

import yaml

from loggingdemo.utils import divide

app_dir = pathlib.Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
log_config_fn = 'logging.yml'
__LOG_CONFIG_PATH = pathlib.Path(app_dir / log_config_fn)

with open(__LOG_CONFIG_PATH, 'rt') as f:
    log_config = yaml.safe_load(f)
logging.config.dictConfig(log_config)

log = logging.getLogger(__name__)

numbers = [1, 2, 3.5, 0]
log.info('Divide all combinations (include zero in the mix)')
for n, d in itertools.combinations(numbers, 2):
    divide_result = divide(n, d)
    print(f'Dividing {n} by {d}\tGives {divide_result}')

log.info('Script complete')
