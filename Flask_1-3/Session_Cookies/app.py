from flask import Flask, redirect, url_for, render_template, request, session, make_response
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "secretkey"  # used for session data encryption
# app.permanent_session_lifetime = timedelta(days=5)  # sets permanent_session in temp file on server

# home page
@app.route("/")
@app.route("/home")
def home():
    resp = make_response(render_template("index.html", title="Home"))
    resp.set_cookie("username", "", expires=0)  # deletes username cookie when returning home
    return resp

# add session info page that checks if POST or GET request
@app.route("/addsession", methods=["POST", "GET"])
def addsession():
    if request.method == "POST":
        # session.permanent = True  # sets to permanent (in this case 5 days)
        user = request.form["nm"]  # gets users name from POST
        session["user"] = user  # creates session variable

        resp = make_response(redirect(url_for("success")))
        resp.set_cookie("username", user)

        return resp  # redirect(url_for("success"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("addsession.html", title="Add Session")

# successfully created session page
@app.route("/success")
def success():
    return render_template("success.html", title="Success")


# verify session data working
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", title="User", username=user)
    else:
        cookie_name = request.cookies.get("username")  # gets username from cookie
        return render_template("user.html", title="User", cookie_name=cookie_name)

# removes session data and redirects back to show user page (jinja2 if/else in html)
@app.route("/clear")
def clear():
    session.pop("user", None)  # remove user from session dictionary 
    return redirect(url_for("user", title="User"))


if __name__ == "__main__":
    app.run(debug=True)
