from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import render_template
from tasks import TASKS
from users import USERS

app = Flask(__name__)

@app.route("/login/form")
def login_form():
    return render_template('login_form.html')

@app.route("/login", methods=['POST'])
def login():
    if request.form['username'] in USERS and USERS[request.form['username']] == request.form['password']:
        response = make_response(redirect("/", code=302))
        response.set_cookie('islogged', 'TRUE')
        response.set_cookie('username', request.form['username'])
        return response
    else:
        return redirect("/login/form", code=302)

@app.route("/")
def showtasks():
    if request.cookies.get('islogged'):
        username = request.cookies.get('username')
        tasks = []
        for task in TASKS:
            if task["owner"] == username:
                tasks.append(task)
        return render_template('tasks.html', username = username, tasks = tasks)
    else:
        return redirect("/login/form", code=302)

@app.route("/addtask/form")
def add_task_form():
    return render_template('add_task.html')

@app.route("/addtask", methods=['POST'])
def add_task():
    new_task = {
        "owner": request.cookies.get('username'),
        "title": request.form['task_name'],
        "date": request.form['task_date'],
        "isopen": "True",
    }
    TASKS.append(new_task)
    response = make_response(redirect("/", code=302))
    return response

app.run(debug=True)
#app.run(host="0.0.0.0", port=80)