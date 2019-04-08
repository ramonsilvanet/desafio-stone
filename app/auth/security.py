from app.auth import auth, secure_key
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


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
    s = Serializer(secure_key)
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
