from .base import FORMATTERS, CONSOLE_HANDLER, file_handler


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': FORMATTERS,
    'handlers': {
        'console': CONSOLE_HANDLER,
        'file': file_handler(filename='local.log', level='DEBUG'),  # this is the main log file by default
        # You can add different log files for each app here e.g
        # 'file.app_name': file_handler(filename='app_name.log', level='DEBUG')
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # You can add app log files handlers here as seen here:
        # 'app_name': {
        #     'handlers': ['console', 'file.app_name'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}
