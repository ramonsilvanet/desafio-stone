import os 

class Config(object):
    SECURE_KEY = os.environ.get('SECURE_KEY')
    SESSION_TIMEOUT = int(os.environ.get('SESSION_TIMEOUT'))
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')