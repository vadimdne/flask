from flask import Flask
from flask import request
from flask import redirect
from flask import make_response

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
def hello():
    if request.cookies.get('islogged'):
        return "Hello World!"
    else:
        return redirect("/login/form", code=302)

@app.route("/login")
def login():
    if request.form['username'] in USERS and USERS[request.form['username']] == request.form['password']:
        response = make_response(redirect("/", code=302))
        response.set_cookie('islogged', 'TRUE')
        return response
    else:
        return redirect("/login/form", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)