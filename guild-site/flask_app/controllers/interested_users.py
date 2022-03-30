import re
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.interested_user import Interested_User

@app.route("/info_request")
def info_request():
    return render_template('info_request.html')

@app.route('/request_submitted', methods = ['POST'])
def info_requested():
    if not Interested_User.validate_user(request.form):
        return redirect ('/info_request')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "phone_number" : request.form['phone_number']
    }
    Interested_User.save(data)
    return redirect('/post_info')
    
@app.route('/post_info')
def post_info():
    return render_template('post_info.html')
