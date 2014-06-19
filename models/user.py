
import pymongo

from app import db

def fetchOneUser(login):
    user = db.users.find_one({'name' : login })
    return user
