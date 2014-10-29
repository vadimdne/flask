__author__ = 'vti'
from flask import request
from flask import redirect
from flask import make_response
from helpers.auth import authorized


class Controller(object):
    def __init__(self, user_model_cls):
        self.user_model_cls = user_model_cls

    @authorized
    def handle_request(self):
        session_id = request.cookies.get('session_id')
        self.user_model_cls.drop_session(session_id)
        response = make_response(redirect("/", code=302))
        return response