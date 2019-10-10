from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, validators, widgets
from application.ingredients.models import Ingredient


class RecipeForm(FlaskForm):
   
    name = StringField("Reseptin nimi", [validators.Length(min=2, max=20)])
    difficult = SelectField(u'Vaikeustaso', choices=[('Helppo','Helppo'),('Keskitaso','Keskitaso'),('Vaikea','Vaikea')])
    event = SelectField(u'Tilaisuus', choices=[('Arki','Arki'),('Juhla','Juhla')]) 
    recipeingredients = SelectMultipleField(u'Ainesosat', coerce=int, widget=widgets.ListWidget(prefix_label=True),
        option_widget=widgets.CheckboxInput())
    
    text = StringField("Ohje", [validators.DataRequired()])
   
    def set_choices(self):
        self.recipeingredients.choices = [(i.id, i.name) for i in Ingredient.query.all()]
    
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    choices = [("Nimi", "Nimi"), ("Vaikeustaso", "Vaikeustaso"), ("Tilaisuus", "Tilaisuus")]
    select = SelectField("Etsi reseptiä:", choices=choices)
    
    search = StringField("", [validators.DataRequired()])

    class Meta:
        csrf = False