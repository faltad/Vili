from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort


from .login import requiresLogin
from app import app

from models import user
from forms import userProfileForm

@app.route('/profile', methods=['GET'])
@requiresLogin
def profile_page():
    profUser = user.fetchOneById(session["id"])
    form = userProfileForm.UserProfileForm()
    return render_template('profile.html', user=profUser, form=form)


@app.route('/profile', methods=['POST'])
@requiresLogin
def profile_update_page():
    profUser = user.fetchOneById(session["id"])
    form = userProfileForm.UserProfileForm(request.form)
    if form.validate():
        profUser.update(form)
    return render_template('profile.html', user=profUser, form=form)

