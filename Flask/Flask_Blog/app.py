from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# key for WT Forms CRF Token
app.config["SECRET_KEY"] = "639ded68629a54ac"

# SQLite development database // use PostgreSQL for production
app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite:////site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        "author": "Stephen Freed",
        "title": "My First Post",
        "content": "My First Post Content",
        "date_posted": "Get Date..."
    },
    {
        "author": "Some Else",
        "title": "My Second Post",
        "content": "My Second Post Content",
        "date_posted": "Get Date..."
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


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
