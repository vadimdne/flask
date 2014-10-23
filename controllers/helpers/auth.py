__author__ = 'vti'
from functools import wraps
from flask import request
from flask import redirect

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get('islogged') != 'true':
            return redirect("/login/form", code=302)
        return f(*args, **kwargs)
    return decorated_function