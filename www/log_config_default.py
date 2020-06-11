# log_config_default.py

import logging.config
import os
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")


config = {
    'version': 1,
    'formatters': {
        'simple1': {
            'format': '%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s'
        },
        'simple2': {
            'format': '%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple1'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': '../logs/python3_web.log',
            'level': 'DEBUG',
            'formatter': 'simple2'
        }
    },
    'loggers': {
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'FileLogger': {
            # 'handlers': ['console', 'file'],
            'handlers': ['file'],
            'level': 'DEBUG'
        }
    }
}


logging.config.dictConfig(config)
StreamLogger = logging.getLogger('StreamLogger')
FileLogger = logging.getLogger('FileLogger')
# FileLogger.disabled = True
