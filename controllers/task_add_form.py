__author__ = 'vti'
from flask import render_template
from helpers.auth import authorized

class Controller(object):
    @staticmethod
    @authorized
    def handle_request(tasklist_id):
        return render_template('task_add.html', tasklist_id=tasklist_id)