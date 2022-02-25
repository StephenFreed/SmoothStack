from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
