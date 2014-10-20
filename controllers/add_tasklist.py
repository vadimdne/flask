__author__ = 'vti'
from flask import request
from flask import make_response
from flask import redirect


class Controller(object):
    def __init__(self, user_model_cls):
        self.user_model_cls = user_model_cls

    def handle_request(self):
        user = self.user_model_cls(request.cookies.get('username'))
        user.add_tasklist(request.form['tasklist_name'])
        response = make_response(redirect("/", code=302))
        return response