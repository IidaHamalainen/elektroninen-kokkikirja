from flask_wtf import FlaskForm
from wtforms import StringField

class RecipeForm(FlaskForm):
    name = StringField("Reseptin nimi")
    difficult = StringField("Vaikeus")
 
    class Meta:
        csrf = False