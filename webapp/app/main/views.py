from flask import render_template, flash, request, jsonify
from flask.ext.login import login_required, current_user
from datetime import datetime
from . import main
from .. import mongo

@main.route('/')
@login_required
def index():
    return render_template('index.html',
            current_user=current_user)

@main.route('/verify_booking')
@login_required
def verify_booking():
    '''Check if the event is valid for a particular account, date and etc.'''
    event_title = request.args.get('title', None)
    event_start = request.args.get('start', None)
    event_end = request.args.get('end', None)
    email = request.args.get('email', None)
    if event_start:
        event_start = datetime.strptime(event_start, "%Y-%m-%dT%H:%M")
        event_date = event_start.strftime('%Y-%m-%d')
        print event_start
    if event_end:
        event_end = datetime.strptime(event_end, "%Y-%m-%dT%H:%M")
        print event_end

    validation = {'valid': 'pass'}
    for d in mongo.db.events.find({'date': event_date}):
        if ((event_start == d['start'] and event_end == d['end'])):
                validation['valid'] = 'overlap'

    if validation['valid'] == 'pass':
        mongo.db.events.insert({
            'start': event_start,
            'end': event_end,
            'date': event_date,
            'by': event_title,
            'email': email,
            })

    return jsonify(validation)
    # return render_template('calendar.html')
