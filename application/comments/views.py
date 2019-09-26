from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from application.recipes.forms import SearchForm

from application.comments.forms import CommentForm
from application.comments.models import Comment


@app.route("/recipes/<recipe_id>/comment")
@login_required
def comment_form(recipe_id):
    r = Recipe.query.get(recipe_id)
    
    return render_template("comments/new_comment.html", form = CommentForm(), recipe = r)

@app.route("/comments/<recipe_id>", methods=["POST"])
@login_required
def comment_create(recipe_id):
    form = CommentForm(request.form)
    recipe = Recipe.query.get(recipe_id) 
    

    if not form.validate():
        return render_template("comments/new_comment.html", form = form,  recipe_id = recipe.id)

    comment = Comment(form.comment_text.data)
    comment.account_id = current_user.id
    comment.recipe_id = recipe.id

    db.session().add(comment)
    db.session().commit()
  
    return redirect(url_for("recipes_show_single", recipe_id = recipe.id))