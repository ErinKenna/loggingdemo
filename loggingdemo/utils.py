import logging


def divide(numerator: int, denominator: int):
    log = logging.getLogger(__name__)
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        log.error('ZeroDivision attempted')
        return None
    return result
