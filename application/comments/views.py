from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user

from application.recipes.models import Recipe

from application.comments.forms import CommentForm
from application.comments.models import Comment

#kommentin lisäämnen
@app.route("/recipes/<recipe_id>/comment")
@login_required(role="ANY")
def comment_form(recipe_id):
    r = Recipe.query.get(recipe_id)
    
    return render_template("comments/new_comment.html", form = CommentForm(), recipe = r)

@app.route("/comments/<recipe_id>", methods=["POST"])
@login_required(role="ANY")
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

#kommentin muokkaaminen
@app.route("/comments/edit/<comment_id>", methods=["GET", "POST"] )
@login_required(role="ANY")
def comment_edit(comment_id):

    c = Comment.query.get(comment_id)
    form = CommentForm(formdata=request.form, obj=c)

    if c.account_id != current_user.id:
        return login_manager.unauthorized()

    if request.method == "POST":
        save_changes(c, form)
        return redirect(url_for("recipes_show_single", recipe_id = c.recipe_id))

    return render_template("comments/edit_comment.html", comment = c, form=form)

def save_changes(comment, form, new = False):

    comment.comment_text = form.comment_text.data

    db.session().commit()
    return redirect(url_for("recipes_show_single", recipe_id = comment.recipe_id))

#kommentin poistaminen
@app.route("/comments/delete/<comment_id>", methods=["GET", "POST"] )
@login_required(role="ANY")
def comment_delete(comment_id):

    c = Comment.query.get(comment_id)

    if c.account_id != current_user.id:
        if current_user.user_role == "ADMIN":
            pass
        else:
            return login_manager.unauthorized()

    if request.method == "POST":
        db.session().delete(c)
        db.session().commit()
        return redirect(url_for("recipes_show_single", recipe_id = c.recipe_id))
    
    return render_template("comments/delete_comment.html")