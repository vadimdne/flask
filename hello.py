from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import render_template
from functools import wraps
import sqlite3

DATABASE = "F:\\tasks.db"

app = Flask(__name__)

conn = sqlite3.connect(DATABASE, check_same_thread=False)

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
    username = (request.form['username'],)
    cur = conn.cursor()
    cur.execute('SELECT password FROM user WHERE username=?', username)
    password = cur.fetchone()
    if password == None or request.form['password'] != password[0]:
        return redirect("/login/form", code=302)
    response = make_response(redirect("/", code=302))
    response.set_cookie('islogged', 'true')
    response.set_cookie('username', request.form['username'])
    cur.close()
    return response                             # use same method for setting response object

@app.route("/")
@authorized
def showtasks():
    username = (request.cookies.get('username'),)
    tasks = []
    cur = conn.cursor()
    cur.execute('SELECT id FROM user WHERE username=?', username)
    user_id = cur.fetchone()
    cur.execute('SELECT id FROM tasklist WHERE user_id=?', user_id)
    tasklist_id = cur.fetchone()                                        # handle several tasklists
    t = cur.execute('SELECT id, name FROM task WHERE tasklist_id=?', tasklist_id)
    for task in t:
        tasks.append(
            {
                'id':task[0],
                'name':task[1],
            }
        )
    cur.close()
    return render_template('tasks.html', username=username, tasks=tasks)

@app.route("/task/add/form")
@authorized
def add_task_form():
    return render_template('add_task.html')

@app.route("/task/add", methods=['POST'])
@authorized
def add_task():
    username = (request.cookies.get('username'),)
    task_name = (request.form['task_name'],)
    cur = conn.cursor()
    cur.execute('SELECT id FROM user WHERE username=?', username)
    user_id = cur.fetchone()
    cur.execute('SELECT id FROM tasklist WHERE user_id=?', user_id)
    tasklist_id = cur.fetchone()                                        # introduce model to avoid copypaste
    cur.execute('INSERT INTO task (name, tasklist_id) VALUES (?,?)', (task_name[0], tasklist_id[0]))
    conn.commit()
    cur.close()
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
    conn.close()
    #app.run(host="0.0.0.0", port=80)