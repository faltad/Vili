
from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for

from db import db

from .login import requiresLogin
from app import app


@app.route('/')
@requiresLogin
def index_page():
    em = db.get_db()
    entries = em.users.find({}, {'name': 1})
    return render_template('show_entries.html', entries=entries)

