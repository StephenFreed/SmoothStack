from flask import render_template, url_for, flash, redirect
from app_package.forms import RegistrationForm, LoginForm
from app_package.models import User, Post
from app_package import app

posts = [
    {
        "author": "Stephen Freed",
        "title": "My First Post",
        "content": "My First Post Content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Some Else",
        "title": "My Second Post",
        "content": "My Second Post Content",
        "date_posted": "April 20, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["POST", "GET"])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        flash(f"Account Created For {reg_form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=reg_form)


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@blog.com" and login_form.password.data == "password":
            flash(f"Successful Login {login_form.email.data}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Please Check Username and Password", "danger")

    return render_template("login.html", title="Login", form=login_form)
