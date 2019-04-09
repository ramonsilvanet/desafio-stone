import os
from app import app, celery
from app.auth import auth, security, secure_key

from flask import Flask, jsonify, abort, make_response, request

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

@app.route('/job', methods=['POST'])
def create_job():
    job = celery.bg_job_fibonnacci.delay(5)    
    return jsonify({'job_id' : 'job created !'})

@app.route('/job/<string:job_id>', methods=['POST'])
def get_job():
    return jsonify({'message' : 'job created !'})

@app.route( '/token', methods=['GET'])
@auth.login_required
def get_key():
    auth_token =  Serializer(secure_key, expires_in = os.environ['SESSION_TIMEOUT'])
    return jsonify({ 'token': auth_token.dumps({ 'id': "1" }).decode('ascii') })

