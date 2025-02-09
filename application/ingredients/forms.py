from flask_wtf import FlaskForm
from wtforms import StringField, validators


class IngredientForm(FlaskForm):
    name = StringField("Raaka-aine", [validators.Length(min=2, max=144)])
   
    class Meta:
        csrf = False