
import pymongo

from app import db

def fetchOneUser(login):
    dbUser = db.users.find_one({'name' : login })
    if dbUser == None:
        return None
    user = User(dbUser, db)
    return user

def fetchOneUserPerEmail(email):
    dbUser = db.users.find_one({'email' : email })
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

def getNewUser():
    dbInfos = db.users.find({}, {"id" : 1}).sort("id", -1)
    if dbInfos == None:
        newId = 1
    else:
        newId = int(dbInfos[0]["id"]) + 1
    print(dbInfos[0])
    print("ID:[%d]" % newId)
    dbUser = dict({"id" : newId})
    user = User(dbUser, db)
    return user

class User():
    def __init__(self, dbUser, db):
        self.id = dbUser["id"]
        self.db = db

        if "password" in dbUser:
            self.password = dbUser["password"]
        else:
            self.password = ""
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

    def update(self):
        db.users.update({ "id" : self.id }, { '$set' : { "surname" : self.surname, "name" : self.name, "title" : self.title, "email" : self.email, "address" : self.address, "city" : self.city, "country" : self.country, "siret" : self.siret }}, upsert = False)

    def save(self):
        db.users.insert({"id" : self.id, "email" : self.email, "password" : self.password})
