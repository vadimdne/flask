__author__ = 'vti'
from flask import redirect
from flask import request
from flask import make_response


class Controller(object):
    def __init__(self, user_model_cls):
        self.user_model_cls = user_model_cls

    def handle_request(self):
        user = self.user_model_cls(request.form['username'])
        if not user.verify_password(request.form['password']):
            return redirect("/login/form", code=302)
        response = make_response(redirect("/", code=302))
        response.set_cookie('username', user.username)
        response.set_cookie('session_id', user.session_id)
        return response