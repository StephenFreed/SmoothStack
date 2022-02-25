from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretkey"  # user for session data
app.permanent_session_lifetime = timedelta(days=5)


# home rendering index.html template and passing variable
@app.route("/")
def home():
    return render_template("index.html", app_var="Flask Application Home Page")


# rendering path name
@app.route("/<name>")
def name(name):
    return f"<h1>Hello {name}<h1>"


# admin page rediriecting and passing name to user page
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))


# login page that checks POST or GET request
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # session.permanent = True  # can set session data to be stored
        user = request.form["nm"]  # gets users name
        session["user"] = user  # creates session variable
        return redirect(url_for("success", name=user))
    else:
        return render_template("login.html")


# login success page
@app.route("/success/<name>")
def success(name):
    return f"<h1>Successful Sign Up {name}</h1>"


# verify session data working
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>You are logged in {user}</h1>"
    else:
        return "<h1>You Are Not Logged In</h1>"


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("user"))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(port=8080, host="0.0.0.0", debug=True)
