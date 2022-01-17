from flask import request,redirect
from functools import wraps
import jwt
import os

SECRET_KEY = os.environ.get("SECRET_KEY")

def login_required(f):
    @wraps(f)
    def wrapper(*args):
        token_receive = request.cookies.get('token')
        try:
            jwt.decode(token_receive, SECRET_KEY , algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return redirect('/login')
        except jwt.exceptions.DecodeError:
            return redirect('/login')
        return f(*args)
    return wrapper

def logout_required(f):
    @wraps(f)
    def wrapper(*args):
        token_receive = request.cookies.get('token')
        try:
            jwt.decode(token_receive, SECRET_KEY , algorithms=['HS256'])
            return redirect('/')
        except:
            pass
        return f(*args)
    return wrapper
