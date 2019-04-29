from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
from app import app

auth = HTTPBasicAuth()

secure_key =  app.config['SECURE_KEY']
auth_token = None

@app.route( '/token', methods=['GET'])
@auth.login_required
def get_key():    
    auth_token =  Serializer(app.config['SECURE_KEY'], expires_in=app.config['SESSION_TIMEOUT'])
    return jsonify({ 'token': auth_token.dumps({"username": "stone pagamentos"}).decode('ascii')})

# Authentication and Authorization
@auth.verify_password
def check_credentials_and_give_a_token(username_or_token, password):
    
    valid = verify_token(username_or_token)
    if not valid :
        if not username_or_token == 'stone' or not password == 'pagamentos':
            return False
        else:
            return True
    else:
        return True


def verify_token(token):
    s = Serializer(app.config['SECURE_KEY'])
    try:
        data = s.loads(token)
        
        if data['id'] == '1':
            return True
        else:
            return None

    except SignatureExpired:
        return None
    except BadSignature:
        return None
    