__author__ = 'vti'
from flask import render_template


class Controller(object):
    @staticmethod
    def handle_request():
        return render_template('login_form.html')