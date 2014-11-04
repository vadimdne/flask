__author__ = 'vti'
from functools import wraps
from flask import request
from flask import redirect
from models.session import Session

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_id = request.cookies.get('session_id')
        if not Session.verify_session(session_id):
            return redirect("/login/form", code=302)
        Session.refresh_session(session_id)
        return f(*args, **kwargs)
    return decorated_function