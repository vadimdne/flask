__author__ = 'vti'
from flask import render_template


class Controller(object):
    @staticmethod
    def handle_request():
        return render_template('tasklist_add.html')
