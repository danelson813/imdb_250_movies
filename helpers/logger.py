# logger.py
import logging
import logging.config
import yaml


def loggerStartup():
    with open('helpers/config.yaml', 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


if __name__ == '__main__':
    logger = loggerStartup()
    logger.info('This is an info message')
    logger.error('This is an error message')
