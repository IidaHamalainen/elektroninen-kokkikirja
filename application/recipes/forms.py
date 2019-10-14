from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, validators, widgets
from application.ingredients.models import Ingredient


class RecipeForm(FlaskForm):
   
    name = StringField("Reseptin nimi", [validators.Length(min=2, max=144)])
    difficult = SelectField(u'Vaikeustaso', choices=[('Helppo','Helppo'),('Keskitaso','Keskitaso'),('Vaikea','Vaikea')])
    event = SelectField(u'Tilaisuus', choices=[('Arki','Arki'),('Juhla','Juhla')]) 
    
    text = StringField("Ohje", [validators.DataRequired(), validators.Length(max=1000)])
    
    ingredients = SelectMultipleField("Aineet", coerce=int, choices=[])

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    choices = [("Nimi", "Nimi"), ("Vaikeustaso", "Vaikeustaso"), ("Tilaisuus", "Tilaisuus"),("Ainekset", "Ainekset")]
    select = SelectField(u'Etsi reseptiä', choices=choices)
    
    search = StringField("", [validators.DataRequired()])

    class Meta:
        csrf = False