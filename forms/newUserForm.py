from wtforms import Form, BooleanField, TextField, PasswordField, validators

class NewUserForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=70)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
