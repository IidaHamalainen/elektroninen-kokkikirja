from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from application.recipes.forms import SearchForm

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/search", methods=["GET", "POST"])
def recipes_search():
    search = SearchForm(request.form)
    if request.method == "POST":
        return recipes_results(search)

    return render_template("recipes/search.html", form = SearchForm())

@app.route("/recipes/results", methods=["GET"])
def recipes_results(search):
    results = []
    search_string = search.data["search"]

    if search_string:
        if search.data["select"] == "Nimi":
            results = Recipe.query.filter(Recipe.name.contains(search_string)).all()
    
    if search_string:
        if search.data["select"] == "Vaikeustaso":
            results = Recipe.query.filter(Recipe.difficult.contains(search_string)).all()        

    if search_string:
        if search.data["select"] == "Tilaisuus":
            results = Recipe.query.filter(Recipe.event.contains(search_string)).all()
    
    if search.data["search"] == "":
        qry = db_session.query(Recipe)
        results = qry.all()
 
    if not results: 
        return redirect(url_for("recipes_index"))

    else:
        return render_template("recipes/list.html", recipes=results)


@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipes_show_single(recipe_id):
   
    s = Recipe.query.get(recipe_id)
    
    return render_template("recipes/single.html", recipe = s)

@app.route("/recipes/<recipe_id>/edit", methods=["GET", "POST"])
def recipe_edit(recipe_id):
    r = Recipe.query.get(recipe_id)
    form = RecipeForm(formdata=request.form, obj=r)

    if request.method == "POST":
        save_changes(r, form)
        return redirect(url_for("recipes_index"))

    return render_template("recipes/edit.html", recipe = r, form=form)

@app.route("/recipes/", methods=["POST"])
def recipes_create():
    form = RecipeForm(request.form)

    r = Recipe(form.name.data)
    r.difficult = form.difficult.data
    r.event = form.event.data

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/delete/<recipe_id>", methods=["GET", "POST"])
def delete(recipe_id):
    r = Recipe.query.get(recipe_id)

    if request.method == "POST":
        db.session().delete(r)
        db.session().commit()
        return redirect(url_for("recipes_index"))
    return render_template("recipes/delete_recipe.html")

def save_changes(recipe, form, new = False):
    
    recipe.name = form.name.data
    recipe.difficult = form.difficult.data
    recipe.event = form.event.data

    db.session().commit()
    return redirect(url_for("recipes_index"))
