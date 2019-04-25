import os 

class Config(object):
    SECURE_KEY = os.environ.get('SECURE_KEY')
    SESSION_TIMEOUT = int(os.environ['SESSION_TIMEOUT'])