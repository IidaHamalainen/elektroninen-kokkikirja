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
@login_required(role="ANY")
def ingredient_create():
    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredient/new_ingredient.html", form = IngredientForm())

    ingredient = Ingredient(form.name.data)

    db.session().add(ingredient)
    db.session().commit()

    return redirect(url_for("ingredients_list"))

@app.route("/ingredients/list", methods=["GET"])
def ingredients_list():
    return render_template("ingredient/all_ingredients.html", ingredients = Ingredient.query.all())

@app.route("/ingredient/delete/<ingredient_id>", methods=["GET", "POST"])
@login_required(role="ANY")
def ingredient_delete(ingredient_id):

    i = Ingredient.query.get(ingredient_id)

    if request.method == "POST":
        db.session().delete(i)
        db.session().commit()
        return redirect(url_for("ingredients_list"))
    
    return render_template("ingredient/delete_ingredient.html")

