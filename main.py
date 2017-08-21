from flask import Flask, render_template, request, redirect
import cgi

import os

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def validation():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    user_error = ""
    pass_error = ""
    ver_pass_error = ""
    email_error = ""

    if username == "" or len(username) < 3 or len(username) >20:
        user_error = "Invalid username"
        #username = ""

    if password == "" or len(password) < 3 or len(password) >20:
        pass_error = "Invalid password"
        password = ""

    if verify_password != password:
        ver_pass_error = "Password's do not match"
        verify_password = ""
    if verify_password == password:
        ver_pass_error = ""

    if "@" not in email and "." not in email or len(email) < 3 or len(email) >20:
        email_error = "Not a valid email address"
    if email == "":
        email_error = ""

    if not user_error and not pass_error and not ver_pass_error and not email_error:
        return render_template("welcome_page.html", username=username)
    else:
        return render_template('index.html',user_error=user_error,
                               pass_error=pass_error,
                               ver_pass_error=ver_pass_error,
                               email_error=email_error,
                               username=username,
                               password=password,
                               verify_password=verify_password,
                               email=email)

@app.route("/welcome")
def welcome():

    pass

app.run()
