from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, PasswordField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=30)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=2, max=15)])
    password = PasswordField("Salasana", [validators.Length(min=4)])

    class Meta:
        csrf = False