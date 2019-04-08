import os
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

secure_key =  os.environ['SECURE_KEY']
auth_token = None