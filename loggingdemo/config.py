import os
import pathlib
import logging.config

import yaml


def log_config():
    app_dir = pathlib.Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
    log_config_fn = 'logging.yml'
    __LOG_CONFIG_PATH = pathlib.Path(app_dir / log_config_fn)

    with open(__LOG_CONFIG_PATH, 'rt') as f:
        log_config = yaml.safe_load(f)
    logging.config.dictConfig(log_config)
