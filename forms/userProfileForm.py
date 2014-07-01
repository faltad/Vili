from wtforms import Form, BooleanField, TextField, PasswordField, validators

class UserProfileForm(Form):
    surname = TextField('Surname', [validators.Length(min=4, max=70)])
    name = TextField('Name', [validators.Length(min=4, max=70)])
    title = TextField('Title', [validators.Length(min=4, max=70)])
    email = TextField('Email', [validators.Email()])
    siret = TextField('Siret', [validators.Length(min=14, max=14, message="The Siret number is not correct")])
    address = TextField('Address', [validators.Length(min=4, max=70)])
    postcode = TextField('Postcode/City', [validators.Length(min=4, max=70)])
    country = TextField('Country', [validators.Length(min=4, max=70)])
    
