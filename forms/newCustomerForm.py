from wtforms import Form, BooleanField, TextField, PasswordField, validators

class NewCustomerForm(Form):
    name = TextField('Name', [validators.Length(min=4, max=70)])
    address = TextField('Address', [validators.Length(min=4, max=200)])
    city = TextField('City/Postcode', [validators.Length(min=4, max=70)])
    country = TextField('Country', [validators.Length(min=4, max=70)])
