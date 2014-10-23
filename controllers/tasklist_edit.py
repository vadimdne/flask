__author__ = 'vti'
from flask import make_response
from flask import request
from flask import redirect
from helpers.auth import authorized


class Controller(object):
    def __init__(self, tasklist_model_cls):
        self.tasklist_model_cls = tasklist_model_cls

    @authorized
    def handle_request(self, tasklist_id):
        tasklist = self.tasklist_model_cls(tasklist_id)
        tasklist.edit(request.form['tasklist_name'])
        response = make_response(redirect("/", code=302))
        return response