import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.member import Member
from flask_app.models.event import Event

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/registration_page')
def registration_page():
    return render_template('registration.html')

@app.route('/registration_form', methods=['POST'])
def registration_form():
    if not Member.validate_user(request.form):
        return redirect ('/registration_page')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "phone_number" : request.form['phone_number'],
        "password" : pw_hash,
        "permissions" : int(request.form['permissions'])
    }
    Member.save(data)
    return redirect('/login_page')

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    member_in_db = Member.get_by_email(data)
    if not member_in_db:
        flash("Invalid Email/Password")
        return redirect("/login_page")
    if not bcrypt.check_password_hash(member_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login_page')
    session['member_id'] = member_in_db.id
    session['member_name'] = member_in_db.first_name
    session['member_permissions'] = member_in_db.permissions

    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    events = Event.get_all_with_rsvps()
    # for event in events:
    #     data = {
    #         'id' : event.id
    #     }
    #     event.rsvps.append(Event.get_all_rsvps(data))

    return render_template('dashboard.html', events = events)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')