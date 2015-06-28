# -*- coding: UTF-8 -*-

from werkzeug.security import check_password_hash
from flask.ext.login import current_user
from flask import render_template, request, url_for, flash, redirect
from flask.ext.login import login_user, login_required, logout_user
from ..models import User
from .forms import LoginForm
from . import auth
from .. import mongo

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated():
        flash("You've been logged in.")
        redirect(url_for('main.index'))

    if form.validate_on_submit():
        user = mongo.db.users.find_one({'email': form.email.data})
        if user is not None and check_password_hash(user['password'],
                form.password.data):
            login_user(User(user['email'], user['name']), form.remember_me.data)
            return redirect(request.args.get('next')
                    or url_for('main.index'))
        flash('Invalid email or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
