from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import render_template
from functools import wraps
from user import User

# Todo move routes to one place
# Todo close db connection in proper place

app = Flask(__name__)

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get('islogged') != 'true':
            return redirect("/login/form", code=302)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login/form")
def login_form():
    return render_template('login_form.html')

@app.route("/login", methods=['POST'])
def login():
    user = User(request.form['username'])
    password = user.get_password()
    if password == None or password != request.form['password']:            # Todo encrypt password
        return redirect("/login/form", code=302)
    response = make_response(redirect("/", code=302))
    response.set_cookie('islogged', 'true')                                 # Todo fix the ability to hack cookies
    response.set_cookie('username', user.get_username())
    return response

@app.route("/")
@authorized
def showtasks():
    user = User(request.cookies.get('username'))
    tasklist = user.get_first_tasklist()
    tasks = tasklist.get_tasks()                                            # Todo handle several tasklists
    return render_template('tasks.html', username=user.get_username(), tasks=tasks)

@app.route("/task/add/form")
@authorized
def add_task_form():
    return render_template('add_task.html')

@app.route("/task/add", methods=['POST'])
@authorized
def add_task():
    user = User(request.cookies.get('username'))
    tasklist = user.get_first_tasklist()
    tasklist.add_task(request.form['task_name'])
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