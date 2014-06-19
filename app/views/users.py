from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort

from db import db

from .login import requiresLogin
from app import app

@app.route('/profile')
