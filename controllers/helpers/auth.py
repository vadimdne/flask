__author__ = 'vti'
from functools import wraps
from flask import request
from flask import redirect
from models.user import User

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_id = request.cookies.get('session_id')
        if not User.verify_session(session_id):
            return redirect("/login/form", code=302)
        User.refresh_session(session_id)
        return f(*args, **kwargs)
    return decorated_function