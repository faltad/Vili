import yaml
import os
import sys
import bcrypt

from pymongo import MongoClient

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)


def parse_file(filename):
    config = False
    try:
        config_file = open(filename)
        config = yaml.load(config_file)
        config_file.close()
    except IOError:
        print("The file " + filename + " could not be opened.")
    except (yaml.YAMLError, exc):
        print("Error in configuration file:", exc)
    
    if config != False:
        if "db-host" not in config:
            print("Cannot find the value of db-host in the configuration file.");
        elif "db-port" not in config:
            print("Cannot find the value of db-port in the configuration file.");
        elif "db-name" not in config:
            print("Cannot find the value of db-name in the configuration file.");
        else:
            return config
    return False;
        

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

@app.route('/')
def index_page():
    if not session.get('id'):
        return redirect(url_for('login_page'))
    db = get_db()
    entries = db.users.find({}, {'name': 1})
    return render_template('show_entries.html', entries=entries)

@app.route('/login', methods=['GET'])
def login_page():
    if session.get('id'):
        return redirect(url_for('index_page'))

    error = None
    return render_template('login.html', error=error)

@app.route('/login', methods=['POST'])
def try_login_page():
    if session.get('id'):
        return redirect(url_for('index_page'))

    error = True
    if "username" in request.form and "password" in request.form:
        db = get_db()
        user = db.users.find_one({'name' : request.form["username"] })
        if user != None:
            hashed = bcrypt.hashpw(request.form["password"].encode('utf-8'), user["password"].encode('utf-8'))
            if hashed == user["password"].encode('utf-8'):
                session['id'] = user["id"]
                return redirect(url_for('index_page'))

    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout_page():
    session.pop('id', None)
    flash('You were logged out')
    return redirect(url_for('login_page'))


config = parse_file("config/config.yml")
if config != False:
    config["SECRET_KEY"] = "dev key"
    app.config.update(config)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5554, debug=True)
