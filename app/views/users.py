import bcrypt
from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort


from .login import requiresLogin
from app import app

from models import user
from forms import userProfileForm
from forms import newUserForm

@app.route('/profile', methods=['GET'])
@requiresLogin
def profile_page():
    profUser = user.fetchOneById(session["id"])
    form = userProfileForm.UserProfileForm(obj=profUser)
    return render_template('profile.html', user=profUser, form=form, error=False)


@app.route('/profile', methods=['POST'])
@requiresLogin
def profile_update_page():
    profUser = user.fetchOneById(session["id"])
    form = userProfileForm.UserProfileForm(request.form)
    error = False
    if form.validate():
        checkEmailUser = user.fetchOneUserPerEmail(form.email.data)
        if checkEmailUser == None or session["id"] == checkEmailUser.id:
            form.populate_obj(profUser)
            profUser.update()
            flash('Your profile has been updated!')
        else:
            error = True
    return render_template('profile.html', user=profUser, form=form, error=error)


@app.route('/profile/new', methods=["GET"])
def new_account_page():
    form = newUserForm.NewUserForm()
    return render_template('new_account.html', form=form, error=False)

@app.route('/profile/new', methods=["POST"])
def create_account_page():
    error = False
    form = newUserForm.NewUserForm(request.form)
    if form.validate():
        if user.fetchOneUserPerEmail(form.email.data) == None:
            profUser = user.getNewUser()
            salt = bcrypt.gensalt()
            form.populate_obj(profUser)
            hashpw = bcrypt.hashpw(profUser.password.encode("utf-8"), salt)
            profUser.password = hashpw.decode()
            profUser.save()
            if session.get('id'):
                flash('The user has been successfully created!')
            else:
                flash('Account successfully created, please login.')
        else:
            error = True
    return render_template('new_account.html', form=form, error=error)
