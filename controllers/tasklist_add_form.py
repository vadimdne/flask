__author__ = 'vti'
from flask import render_template
from helpers.auth import authorized


class Controller(object):
    @authorized
    def handle_request(self):
        return render_template('tasklist_add.html')
