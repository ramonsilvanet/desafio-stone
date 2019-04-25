import os
from app import app, celery
from app.auth import auth, security, secure_key

from flask import Flask, jsonify, abort, make_response, request

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)



@app.route( '/token', methods=['GET'])
@auth.login_required
def get_key():    
    auth_token =  Serializer(secure_key, expires_in=int(os.environ['SESSION_TIMEOUT']))
    return jsonify({ 'token': auth_token.dumps({"username": "stone pagamentos"}).decode('ascii')})
