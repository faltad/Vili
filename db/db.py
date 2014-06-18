
from pymongo import MongoClient

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from app import app

def connect_db():
    try :
        client = MongoClient(app.config["db-host"], app.config["db-port"])
    except:
        print("Connection to the database refused.")
        return False
    return client

def get_db():
    if not hasattr(g, 'client'):
        g.client = connect_db()
    return g.client[app.config["db-name"]]

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'client'):
        g.client.close()
