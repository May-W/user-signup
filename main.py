from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login_form.html')

@app.route('/', methods=['POST'])

def validate_form():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password2_error = ''
    email_error = ''


    if is_blank(username) == True:
        username_error = "Username must not be blank"
    elif length_valid(username) == False or contains_spaces(username) == True:
        username_error = "Username must be between 3 and 20 characters and must not contain spaces"
    
    if is_blank(password) == True:
        password_error = "Password must not be blank"
    elif length_valid(password) == False or contains_spaces(password) == True:
        password_error = "Password must be between 3 and 20 characters and must not contain spaces"

    if is_blank(password2) == True:
        password2_error = "Password must not be blank"
    elif length_valid(password2) == False or contains_spaces(password2) == True:
        password2_error = "Password must be between 3 and 20 characters and must not contain spaces"

    if password != password2:
        password_error: "Passwords must Match"
        password2_error = "Passwords must match"

    if len(email) != 0:
        if length_valid(email) == False or contains_spaces(email) == True or one_at(email) == False or one_dot(email) == False:
            email_error = "Email must be between 3 and 20 characters, must not contain spaces, and may only contain one at and one dot"

    if not username_error and not password_error and not password2_error and not email_error:
        return redirect('/welcome?name={0}'.format(username))
    else: 
        return render_template('login_form.html', username_error = username_error, password_error = password_error, password2_error = password2_error, email_error = email_error, username=username, password='', password2='', email=email)


def is_blank(string):
    if len(string) == 0:
        return True

def length_valid(string):
    if len(string) > 20 or len(string) < 3:
        return False
    else:
        return True

def contains_spaces(string):
    spaces = 0
    for c in string:
        if c == ' ':
            spaces = spaces + 1
    if spaces > 0:
        return True
    else:
        return False

def one_at(string):
    at = 0
    for c in string:
        if c == '@':
            at = at + 1
    if at == 1:
        return True
    else:
        return False

def one_dot(string):
    dot = 0
    for c in string:
        if c == '.':
            dot = dot + 1
    if dot == 1:
        return True
    else:
        return False


@app.route('/welcome')
def welcome():
    username = request.args.get('name')
    return render_template('welcome.html', title="Welcome!", username=username)

app.run()
