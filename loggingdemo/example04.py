""" Refactor logging config into it's own module.
"""

import itertools
import logging.config

from loggingdemo.utils import divide
from loggingdemo.config import log_config

log_config()


def main(numbers):
    log = logging.getLogger(__name__)

    log.info('Divide all combinations')
    for n, d in itertools.permutations(numbers, 2):
        divide_result = divide(n, d)
        print(f'Dividing {n} by {d}\tGives {divide_result}')
    log.info('All combinations calculated')


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.info('Running as script')

    main(numbers=[1, 2, 3.5, 0])

    log.info('Script complete')
