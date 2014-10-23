__author__ = 'vti'
from flask import redirect
from flask import make_response


class Controller(object):
    def handle_request(self):
        response = make_response(redirect("/", code=302))
        response.set_cookie('islogged', 'false')
        return response