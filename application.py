from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import render_template
from functools import wraps
from user import User
from tasklist import Tasklist
from task import Task

# Todo move routes to one place
# Todo close db connection in proper place
# Todo move controllers in separate files
# Todo use url_for in views

app = Flask(__name__)

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get('islogged') != 'true':
            return redirect("/login/form", code=302)
        return f(*args, **kwargs)
    return decorated_function

from controllers import login_form
app.add_url_rule("/login/form", endpoint="login_form", view_func=login_form.Controller.handle_request)

@app.route("/login", methods=['POST'])
def login():
    user = User(request.form['username'])
    password = user.get_password()
    if password == None or password != request.form['password']:            # Todo encrypt password
        return redirect("/login/form", code=302)
    response = make_response(redirect("/", code=302))
    response.set_cookie('islogged', 'true')                                 # Todo fix the ability to hack cookies
    response.set_cookie('username', user.username)
    return response

@app.route("/")
@authorized
def showtasks():
    user = User(request.cookies.get('username'))
    tasklists = user.get_tasklists()
    return render_template('tasks.html', user=user, tasklists=tasklists)

@app.route("/tasklist/add/form")
@authorized
def add_tasklist_form():
    return render_template('add_tasklist.html')

from controllers import add_tasklist
add_tasklist_controller = add_tasklist.Controller(User)
app.add_url_rule("/tasklist/add", endpoint="add_tasklist", view_func=authorized(add_tasklist_controller.handle_request), methods=['POST'])

@app.route("/tasklist/edit/form/<int:tasklist_id>")
@authorized
def edit_tasklist_form(tasklist_id):
    tasklist = Tasklist(tasklist_id)
    return render_template('edit_tasklist.html', tasklist=tasklist)

@app.route("/tasklist/edit/<int:tasklist_id>", methods=['POST'])
@authorized
def edit_tasklist(tasklist_id):
    tasklist = Tasklist(tasklist_id)
    tasklist.edit(request.form['tasklist_name'])
    response = make_response(redirect("/", code=302))
    return response

@app.route("/task/add/form/<int:tasklist_id>")
@authorized
def add_task_form(tasklist_id):
    return render_template('add_task.html', tasklist_id=tasklist_id)

@app.route("/task/add/<int:tasklist_id>", methods=['POST'])
@authorized
def add_task(tasklist_id):
    tasklist = Tasklist(tasklist_id)
    tasklist.add_task(request.form['task_name'])
    response = make_response(redirect("/", code=302))
    return response

@app.route("/task/edit/form/<int:task_id>")
@authorized
def edit_task_form(task_id):
    task = Task(task_id)
    return render_template('edit_task.html', task=task)

@app.route("/task/edit/<int:task_id>", methods=['POST'])
@authorized
def edit_task(task_id):
    task = Task(task_id)
    task.edit(request.form['task_name'])
    response = make_response(redirect("/", code=302))
    return response

@app.route("/task/delete/<int:task_id>")
@authorized
def delete_task(task_id):
    task = Task(task_id)
    task.delete()
    response = make_response(redirect("/", code=302))
    return response

@app.route("/logout")
@authorized
def logout():
    response = make_response(redirect("/", code=302))
    response.set_cookie('islogged', 'false')
    return response

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=80)