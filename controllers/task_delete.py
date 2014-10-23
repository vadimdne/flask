__author__ = 'vti'
from flask import make_response
from flask import redirect
from helpers.auth import authorized


class Controller(object):
    def __init__(self, task_model_cls):
        self.task_model_cls = task_model_cls

    @authorized
    def handle_request(self, task_id):
        task = self.task_model_cls(task_id)
        task.delete()
        response = make_response(redirect("/", code=302))
        return response
