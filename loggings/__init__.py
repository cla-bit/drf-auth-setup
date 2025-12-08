import os


DJANGO_ENV = os.getenv('DJANGO_ENV').lower()

if DJANGO_ENV == 'production':
    from .production import LOGGING
elif DJANGO_ENV == "staging":
    from .staging import LOGGING
else:
    from .local import LOGGING
