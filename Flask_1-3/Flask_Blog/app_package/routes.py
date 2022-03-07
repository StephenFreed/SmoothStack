from flask import render_template, url_for, flash, redirect, request, abort
from app_package.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from app_package.models import User, Post
from app_package import application, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
import os
import secrets
from PIL import Image


@application.route("/")
@application.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", title="Home", posts=posts)


@application.route("/about")
def about():
    return render_template("about.html", title="About")


# register new user
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


# user can login
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


# logout user
@application.route("/logout")
def logout():
    logout_user()
    flash("You Have Been Logged Out", "success")
    return redirect(url_for("home"))


# helper function to save picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)  # random hex
    f_name, f_ext = os.path.splitext(form_picture.filename)  # split filename and ext
    picture_fn = random_hex + f_ext  # new file name
    picture_path = os.path.join(application.root_path, "static/profile_pics", picture_fn)  # path to save
    
    # resizes to thumbnail
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)  # saves picture with new name

    return picture_fn


# helper function to remove old picture if not default 
def remove_old_picture(old_filename):
    try:
        path_to_remove = os.path.join(application.root_path, "static/profile_pics", old_filename)
        os.remove(path_to_remove)
    except:
        pass


# user account page
@application.route("/account", methods=["POST", "GET"])
@login_required
def account():
    update_form = UpdateAccountForm()  # user can update account info
    if update_form.validate_on_submit():
        if update_form.picture.data:  # check if picture provided
            picture_file = save_picture(update_form.picture.data)  # names, resizes, and saves new picture
            if picture_file:  # removes old picture if not default
                if current_user.image_file != "default.jpg":
                    remove_old_picture(current_user.image_file)
            current_user.image_file = picture_file  # saves to db new image file name under user
        current_user.username = update_form.username.data
        current_user.email = update_form.email.data
        db.session.commit()
        flash("Your Account Has Been Updated", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":  # fills in user data into form
        update_form.username.data = current_user.username
        update_form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    users = User.query.all()
    admin = "admin"
    return render_template("account.html", title="Account", image_file=image_file, users=users, admin=admin, form=update_form)


# new post page
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


# individual post page by post id
@application.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


# if author of post update page
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


# if author of post delete page
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


# admin account page delete user
@application.route("/delete/<int:user_id>")
@login_required
def delete_user(user_id):
    try:
        if user_id != 1:
            Post.query.filter(Post.user_id == user_id).delete()  # deletes all posts by user

            user_to_delete = User.query.get(user_id)  # gets user info for image
            if user_to_delete.image_file != "default.jpg":
                remove_old_picture(user_to_delete.image_file)
            User.query.filter(User.id == user_id).delete()  # deletes user
            db.session.commit()
            flash("User  and Posts Have Been Deleted", "success")
    except:
        flash("There Was A Problem Deleting User", "danger")
    finally:
        return redirect(url_for("account"))
    

@application.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html"), 404


@application.errorhandler(403)
def error_403(error):
    return render_template("errors/403.html"), 403


@application.errorhandler(500)
def error_500(error):
    return render_template("errors/500.html"), 500
