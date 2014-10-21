__author__ = 'vti'
from flask import render_template
from flask import request


class Controller(object):
    def __init__(self, user_model_cls):
        self.user_model_cls = user_model_cls

    def handle_request(self):
        user = self.user_model_cls(request.cookies.get('username'))
        tasklists = user.get_tasklists()
        return render_template('dashboard.html', user=user, tasklists=tasklists)