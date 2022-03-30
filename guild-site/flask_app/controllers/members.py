import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.member import Member

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")
