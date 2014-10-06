from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import render_template
from tasks import TASKS
from users import USERS
from functools import wraps
import sqlite3


app = Flask(__name__)

# connect to db here

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.cookies.get('islogged'):
            return redirect("/login/form", code=302)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login/form")
def login_form():
    return render_template('login_form.html')

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    if username in USERS:
        password = USERS[request.form['username']]
    else:
        return redirect("/login/form", code=302)

    if request.form['password'] == password:
        response = make_response(redirect("/", code=302))
        response.set_cookie('islogged', 'TRUE')
        response.set_cookie('username', request.form['username'])
        return response #use one same method for setting response object
    else:
        return redirect("/login/form", code=302)

@app.route("/")
@authorized
def showtasks():
    username = request.cookies.get('username')
    tasks = []
    for task in TASKS:
        if task["owner"] == username:
            tasks.append(task)
    return render_template('tasks.html', username=username, tasks=tasks)

@app.route("/task/add/form")
@authorized
def add_task_form():
    return render_template('add_task.html')

@app.route("/task/add", methods=['POST'])
@authorized
def add_task():
    new_task = {
        "owner": request.cookies.get('username'),
        "title": request.form['task_name'],
        "isopen": "True",
    }
    TASKS.append(new_task)
    response = make_response(redirect("/", code=302))
    return response

app.run(debug=True)
#app.run(host="0.0.0.0", port=80)