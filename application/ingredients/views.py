from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm

@app.route("/ingredient/add")
def ingredient_form():
    return render_template("ingredient/new_ingredient.html", form = IngredientForm())

@app.route("/ingredients", methods=["POST"])
def ingredient_create():
    form = IngredientForm(request.form)

    ingredient = Ingredient(form.name.data)

    db.session().add(ingredient)
    db.session().commit()

    return redirect(url_for("index"))

    
