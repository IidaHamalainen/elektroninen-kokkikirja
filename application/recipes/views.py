from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user

from application import app, db, login_manager, login_required

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from application.recipes.forms import SearchForm

from application.comments.forms import CommentForm
from application.comments.models import Comment

from application.ingredients.models import Ingredient

@app.route("/recipes/list", methods=["GET"])
def recipes_list():
    return render_template("recipes/list.html", recipes = Recipe.query.all())


#Reseptien etsiminen
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
    
        elif search.data["select"] == "Vaikeustaso":
            results = Recipe.query.filter(Recipe.difficult.contains(search_string)).all()        
        
        elif search.data["select"] == "Tilaisuus":
            results = Recipe.query.filter(Recipe.event.contains(search_string)).all()
    
    if search.data["search"] == "":
        qry = db_session.query(Recipe)
        results = qry.all()
 
    if not results: 
        flash("Ei tuloksia")
        return redirect(url_for("recipes_search"))

    else:
        return render_template("recipes/list.html", recipes=results)

#Uuden reseptin lisääminen
@app.route("/recipes/new/")
@login_required(role="ANY")
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

#Yksittäisen reseptin näyttäminen
@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipes_show_single(recipe_id):

    s = Recipe.query.get(recipe_id)
    comments = Comment.query.join(Recipe).filter(Recipe.id == s.id)
    
    return render_template("recipes/single.html", recipe = s, comments=comments)

#Reseptin muokkaaminen
@app.route("/recipes/<recipe_id>/edit", methods=["GET", "POST"])
@login_required(role="ANY")
def recipe_edit(recipe_id):
    r = Recipe.query.get(recipe_id)
    form = RecipeForm(formdata=request.form, obj=r)

    if r.account_id != current_user.id:
        if current_user.user_role == "ADMIN":
            pass
        else:
            return login_manager.unauthorized()

    if request.method == "POST":
        save_changes(r, form)
        return redirect(url_for("recipes_list"))

    return render_template("recipes/edit.html", recipe = r, form=form)

def save_changes(recipe, form, new = False):
    
    recipe.name = form.name.data
    recipe.difficult = form.difficult.data
    recipe.event = form.event.data
    recipe.text = form.text.data

    db.session().commit()
    return redirect(url_for("recipes_list"))


#Reseptin luominen tietokantaan
@app.route("/recipes/", methods=["POST"])
@login_required(role="ANY")
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data, form.text.data)
    r.difficult = form.difficult.data
    r.event = form.event.data
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_list"))

#reseptin poistaminen
@app.route("/delete/<recipe_id>", methods=["GET", "POST"])
@login_required(role="ANY")
def delete(recipe_id):
    r = Recipe.query.get(recipe_id)

    if r.account_id != current_user.id:
        if current_user.user_role == "ADMIN":
            pass
        else:
            return login_manager.unauthorized()

    if request.method == "POST":
        db.session().delete(r)
        db.session().commit()
        return redirect(url_for("recipes_list"))
    return render_template("recipes/delete_recipe.html")


