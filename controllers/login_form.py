__author__ = 'vti'
from flask import render_template

CODECHA_PUBLIC_KEY = "c717b24a797041b79d27e54ed6cee53b"

class Controller(object):
    def handle_request(self):
        codecha_key = CODECHA_PUBLIC_KEY
        return render_template('login.html', codecha_key=codecha_key)