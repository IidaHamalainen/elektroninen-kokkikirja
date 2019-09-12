from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
def recipes_create():
    form = RecipeForm(request.form)

    r = Recipe(form.name.data)
    r.difficult = form.difficult.data

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))
