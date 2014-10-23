__author__ = 'vti'
from flask import render_template
from helpers.auth import authorized

class Controller(object):
    def __init__(self, tasklist_model_cls):
        self.tasklist_model_cls = tasklist_model_cls
    @authorized
    def handle_request(self, tasklist_id):
        tasklist = self.tasklist_model_cls(tasklist_id)
        return render_template('task_add.html', tasklist=tasklist)