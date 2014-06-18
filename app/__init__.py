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
            print("Cannot find the value of 'db-host' in the configuration file.");
        elif "db-port" not in config:
            print("Cannot find the value of 'db-port' in the configuration file.");
        elif "db-name" not in config:
            print("Cannot find the value of 'db-name' in the configuration file.");
        elif "install" not in config:
            print("Cannot find the value of 'install' in the configuration file.");
        else:
            return config
    return False;

from . import views        

config = parse_file("config/config.yml")
if config != False:
    config["SECRET_KEY"] = "dev key"
    app.config.update(config)
