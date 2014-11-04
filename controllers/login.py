__author__ = 'vti'
from flask import redirect
from flask import request
from flask import make_response
from helpers.codecha import Codecha

CODECHA_PRIVATE_KEY = "3856e53084634b6b8e82f9bf26cb6c30"

class Controller(object):
    def __init__(self, user_model_cls, session_model_cls):
        self.user_model_cls = user_model_cls
        self.session_model_cls = session_model_cls

    def handle_request(self):
        user = self.user_model_cls(request.form['username'])
        session = self.session_model_cls(user.id)

        codecha_challenge = request.form['codecha_challenge_field']
        codecha_response = request.form['codecha_response_field']
        codecha_key = CODECHA_PRIVATE_KEY
        ip = request.environ['REMOTE_ADDR']

        if codecha_challenge and codecha_response:
            codecha_success = Codecha.verify(codecha_challenge, codecha_response, ip, codecha_key)
        else:
            codecha_success = False

        if not codecha_success or not user.verify_password(request.form['password']):
            return redirect("/login/form", code=302)

        response = make_response(redirect("/", code=302))
        response.set_cookie('username', user.username)
        response.set_cookie('session_id', session.id)
        return response