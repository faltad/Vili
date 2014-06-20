
import pymongo

from app import db

def fetchOneUser(login):
    user = User(db.users.find_one({'name' : login }))
    return user

def fetchOneById(idUser):
    user = User(db.users.find_one({'id':idUser}))
    return user

class User():
    def __init__(self, dbUser):
        if "surname" in dbUser:
            self.surname = dbUser["surname"]
        else:
            self.surname = ""
        if "name" in dbUser:
            self.name = dbUser["name"]
        else:
            self.name = ""
        if "title" in dbUser:
            self.title = dbUser["title"]
        else:
            self.title = ""
        if "email" in dbUser:
            self.email = dbUser["email"]
        else:
            self.email = ""
        if "address" in dbUser:
            self.address = dbUser["address"]
        else:
            self.address = ""
        if "city" in dbUser:
            self.city = dbUser["city"]
        else:
            self.city = ""
        if "country" in dbUser:
            self.country = dbUser["country"]
        else:
            self.country = ""
        if "siret" in dbUser:
            self.siret = dbUser["siret"]
        else:
            self.siret = ""

