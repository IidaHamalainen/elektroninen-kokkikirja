from application import app, db, login_required
from flask import redirect, render_template
from flask_login import current_user

from application.recipes.models import Recipe
from application.comments.models import Comment
from application.ingredients.models import Ingredient
from application.auth.models import User

@app.route("/statistics")
def show_statistics():
    user_recipes=User.users_recipes()
    most_used=Ingredient.most_used()

    return render_template("statistics/statistics_page.html", user_recipes=user_recipes, most_used=most_used)