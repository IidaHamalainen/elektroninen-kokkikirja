from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField

class RecipeForm(FlaskForm):
    name = StringField("Reseptin nimi")
    difficult = SelectField(u'Vaikeustaso', choices=[('Helppo','Helppo'),('Keskitaso','Keskitaso'),('Vaikea','Vaikea')])
    event = SelectField(u'Tilaisuus', choices=[('Arki','Arki'),('Juhla','Juhla')])
 
    class Meta:
        csrf = False