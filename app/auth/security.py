from flask import current_app

from app.auth import auth, bp
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask import Flask, jsonify, abort, make_response, request


@bp.route( '/token', methods=['GET'])
@auth.login_required
def get_key():    
    auth_token =  Serializer(current_app.config['SECURE_KEY'], expires_in=current_app.config['SESSION_TIMEOUT'])
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
    s = Serializer(current_app.config['SECURE_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    
    if data['id'] == '1':
        return True
    else:
        return None
