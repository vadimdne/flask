__author__ = 'vti'
from flask import render_template
from helpers.auth import authorized


class Controller(object):
    def __init__(self, task_model_cls):
        self.task_model_cls = task_model_cls

    @authorized
    def handle_request(self, task_id):
        task = self.task_model_cls(task_id)
        return render_template('task_edit.html', task=task)