from app import app
from app.auth import auth, security, secure_key

from flask import Flask, jsonify, abort, make_response, request

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from app.workers import worker

@app.route('/job', methods=['POST'])
def create_job():
    w = worker.Worker()
    w.execute(5)
    return jsonify({'message' : 'job {} created !'.format(w.id)})

@app.route('/job/<string:job_id>', methods=['POST'])
def get_job():
    return jsonify({'message' : 'job created !'})



@app.route( '/todo/api/v1.0/token', methods=['GET'])
@auth.login_required
def get_key():
    auth_token =  Serializer(secure_key, expires_in = 600)
    return jsonify({ 'token': auth_token.dumps({ 'id': "1" }).decode('ascii') })

