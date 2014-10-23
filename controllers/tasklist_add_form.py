__author__ = 'vti'
from flask import render_template
from helpers.auth import authorized


class Controller(object):
    @staticmethod
    @authorized
    def handle_request():
        return render_template('tasklist_add.html')
