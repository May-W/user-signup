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
    return "Hello World"

app.run()