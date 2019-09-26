from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators


class RecipeForm(FlaskForm):
    name = StringField("Reseptin nimi", [validators.Length(min=2)])
    difficult = SelectField(u'Vaikeustaso', choices=[('Helppo','Helppo'),('Keskitaso','Keskitaso'),('Vaikea','Vaikea')])
    event = SelectField(u'Tilaisuus', choices=[('Arki','Arki'),('Juhla','Juhla')])
 
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    choices = [("Nimi", "Nimi"), ("Vaikeustaso", "Vaikeustaso"), ("Tilaisuus", "Tilaisuus")]
    select = SelectField("Etsi reseptiä:", choices=choices)
    
    search = StringField("")

    class Meta:
        csrf = False