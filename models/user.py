
import pymongo

from app import db

def fetchOneUser(login):
    dbUser = db.users.find_one({'name' : login })
    if dbUser == None:
        return None
    user = User(dbUser, db)
    return user

def fetchOneById(idUser):
    dbUser = db.users.find_one({'id':idUser})
    if dbUser == None:
        return None
    user = User(dbUser, db)
    return user

class User():
    def __init__(self, dbUser, db):
        self.id = dbUser["id"]
        self.password = dbUser["password"]
        self.db = db
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

    def update(self, formUser):
        self.surname = formUser.surname.data
        self.name = formUser.name.data
        self.title = formUser.title.data
        self.email = formUser.email.data
        self.address = formUser.address.data
        self.city = formUser.postcode.data
        self.country = formUser.country.data
        self.siret = formUser.siret.data
        db.users.update({ "id" : self.id }, { '$set' : { "surname" : self.surname, "name" : self.name, "title" : self.title, "email" : self.email, "address" : self.address, "city" : self.city, "country" : self.country, "siret" : self.siret }}, upsert = False)
