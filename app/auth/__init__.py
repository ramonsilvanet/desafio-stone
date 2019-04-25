import os
from flask_httpauth import HTTPBasicAuth
from flask import Blueprint
bp = Blueprint('auth', __name__)

auth = HTTPBasicAuth()

secure_key =  os.environ['SECURE_KEY']
auth_token = None

from app.auth import security