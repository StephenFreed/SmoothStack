from flask import render_template, url_for, flash, redirect, request, abort
from app_package.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from app_package.models import User, Post
from app_package import application, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required


@application.route("/test")
def test():
    return redirect("http://flaskblog-env.eba-iwefsg4k.us-east-2.elasticbeanstalk.com/")

@application.route("/")
@application.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", title="Home", posts=posts)


@application.route("/about")
def about():
    return render_template("about.html", title="About")


@application.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(reg_form.password.data).decode("utf-8")
        user = User(username=reg_form.username.data, email=reg_form.email.data.lower(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account Created For {reg_form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=reg_form)


@application.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please Check Email and Password", "danger")

    return render_template("login.html", title="Login", form=login_form)


@application.route("/logout")
def logout():
    logout_user()
    flash("You Have Been Logged Out", "success")
    return redirect(url_for("home"))


@application.route("/account", methods=["POST", "GET"])
@login_required
def account():
    update_form = UpdateAccountForm()
    if update_form.validate_on_submit():
        current_user.username = update_form.username.data
        current_user.email = update_form.email.data
        db.session.commit()
        flash("Your Account Has Been Updated", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        update_form.username.data = current_user.username
        update_form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    users = User.query.all()
    admin = "admin"
    return render_template("account.html", title="Account", image_file=image_file, users=users, admin=admin, form=update_form)


@application.route("/post/new", methods=["POST", "GET"])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Post(title=post_form.title.data, content=post_form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your Post Has Been Created", "success")
        return redirect(url_for("home"))
    return render_template("create_post.html", title="New Post", form=post_form, legend="New Post")


@application.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@application.route("/post/<int:post_id>/update", methods=["POST", "GET"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    post_form = PostForm()
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.content = post_form.content.data
        db.session.commit()  # don't have to add since they are already in DB
        flash("Your Post Has Been Updated", "success")
        return redirect(url_for("post", post_id=post.id))
    elif request.method == "GET":
        post_form.title.data = post.title
        post_form.content.data = post.content
    return render_template("create_post.html", title="Update Post", 
        form=post_form, legend="Update Post")


@application.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your Post Has Been Deleted", "success")
    return redirect(url_for("home"))
    
