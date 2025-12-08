from pathlib import Path
from typing import Union


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Dynamically ensure the logs/ directory exists
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(parents=True, exist_ok=True)  # Creates logs/ if not present

FORMATTERS = {
    'verbose': {
        'format': '[{asctime}] {levelname} {name} {message}',
        'style': '{',
    },
    'simple': {
        'format': '{levelname} {message}',
        'style': '{',
    },
}

CONSOLE_HANDLER = {
    'class': 'logging.StreamHandler',
    'formatter': 'simple',
}


def file_handler(filename: Union[str, Path] = 'default.log', level: str = 'DEBUG'):
    return {
        'level': level,
        'class': 'logging.FileHandler',
        'filename': str(LOGS_DIR / filename),
        'formatter': 'verbose',
    }
