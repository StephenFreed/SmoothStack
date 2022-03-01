from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretkey"  # used for session data encryption
# sets permanent_session in temp file on server
app.permanent_session_lifetime = timedelta(days=5)


# home rendering index.html template and passing variable
@app.route("/")
def home():
    return render_template("index.html", app_var="Flask Application Home Page")


# login page that checks POST or GET request
@app.route("/addsession", methods=["POST", "GET"])
def addsession():
    if request.method == "POST":
        session.permanent = True  # sets to permanent
        user = request.form["nm"]  # gets users name
        session["user"] = user  # creates session variable
        return redirect(url_for("success", name=user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("addsession.html")


# login success page
@app.route("/success/<name>")
def success(name):
    return f"<h1>Successful seasion username: {name} now has session data</h1>"


# verify session data working
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>This is returned by session data:  {user}</h1>"
    else:
        return "<h1>You have no session data yet...</h1>"


@app.route("/logout")
def logout():
    session.pop("user", None)  # remove user data from session
    return redirect(url_for("user"))


if __name__ == "__main__":
    app.run(debug=True)
