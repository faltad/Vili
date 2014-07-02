from wtforms import Form, BooleanField, TextField, PasswordField, validators
from forms.validators import siretValidator


class UserProfileForm(Form):
    surname = TextField('Surname', [validators.Length(min=4, max=70)])
    name = TextField('Name', [validators.Length(min=4, max=70)])
    title = TextField('Title', [validators.Length(min=4, max=70)])
    email = TextField('Email', [validators.Email()])
    siret = TextField('Siret', [siretValidator.siretValidator()])
    address = TextField('Address', [validators.Length(min=4, max=70)])
    city = TextField('Postcode/City', [validators.Length(min=4, max=70)])
    country = TextField('Country', [validators.Length(min=4, max=70)])
    
