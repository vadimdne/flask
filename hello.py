from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from tasks import TASKS

USERS = {
    "vadim": "vadim",
    "roman": "roman",
}
app = Flask(__name__)

@app.route("/login/form")
def login_form():
    return """<form action="/login" method="POST">
    username: <input type="text" name="username">
    password: <input type="password" name="password">
    <input type="submit" value="login">
    </form>"""

@app.route("/")
def showtasks():
    if request.cookies.get('islogged'):
        response = "Hello " + request.cookies.get('username') + "! Here are your tasks: \n"
        for task in TASKS:
            if task["owner"] == request.cookies.get('username'):
                response = response + task["title"] + '\n'
        return response
    else:
        return redirect("/login/form", code=302)

@app.route("/login", methods=['POST'])
def login():
    if request.form['username'] in USERS and USERS[request.form['username']] == request.form['password']:
        response = make_response(redirect("/", code=302))
        response.set_cookie('islogged', 'TRUE')
        response.set_cookie('username', request.form['username'])
        return response
    else:
        return redirect("/login/form", code=302)


    app.run(host="0.0.0.0", port=80)