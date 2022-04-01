from flask_app import app
from flask import render_template, request, redirect, session, flash
from pprint import pprint
from flask_app.models.event import Event

@app.route('/rsvp', methods = ["POST"])
def rsvp():
    data = {
        'member_id' : session['member_id'],
        'event_id' : request.form['event_id']
    }
    if(request.form['rsvp-box'] == 'going'):
        Event.save_rsvp(data)

    elif(request.form['rsvp-box'] == 'not'):
        Event.save_non_rsvp(data)

    return redirect('/dashboard')
