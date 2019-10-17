from flask_wtf import FlaskForm
from application.auth.models import User
from wtforms import PasswordField, StringField, PasswordField, validators, ValidationError
  

def validateUniqueUsername(form, field):
    user = User.query.filter_by(username = field.data).first()
    if user:
        raise ValidationError("käyttäjätunnus on jo olemassa")

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=30)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=2, max=15), validateUniqueUsername])
    password = PasswordField("Salasana", [validators.Length(min=4, max=144)])

    class Meta:
        csrf = False