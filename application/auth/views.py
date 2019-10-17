from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, AccountForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    form = LoginForm(request.form)

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
    

    user = User.query.filter_by(username=form.username.data).first()
    if not user or not bcrypt.check_password_hash(user.passwordHash, form.password.data):
        return render_template("auth/loginform.html", form = form,
                               error = "Virheellinen käyttäjätunnus tai salasana")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

#Uuden käyttäjän lisääminen
@app.route("/auth/new/")
def account_form():
    return render_template("auth/new_user.html", form = AccountForm())

#Käyttäjän luominen tietokantaan
@app.route("/auth/", methods=["POST"])
def account_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("auth/new_user.html", form = form)

    account = User(form.name.data, form.username.data, form.password.data, user_role = "ADMIN")
   

    db.session().add(account)
    db.session().commit()
  
    return redirect(url_for("index"))