from flask import render_template, flash
from flask.ext.login import login_required, current_user
from . import main

@main.route('/')
@login_required
def index():
    return render_template('index.html',
            current_user=current_user)

@login_required
def calendar():
    return render_template('calendar.html')
