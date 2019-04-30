import os
from flask import Flask

app = Flask(__name__)

#Configuracoes do app
app.config.update(
    SECURE_KEY = os.environ['SECURE_KEY'],
    SESSION_TIMEOUT = int(os.environ['SESSION_TIMEOUT']),
    REDIS_URL=os.environ['REDIS_URL'],
    REDIS_QUEUE=os.environ['REDIS_QUEUE'],
    TESTING=os.environ['TESTING']
)

from app import routes, errors, authentication