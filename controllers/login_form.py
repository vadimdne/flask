__author__ = 'vti'
from flask import render_template


class Controller(object):
    def handle_request(self):
        return render_template('login.html')