from flask import Flask, render_template
import requests

all_posts = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<id>")
def view_post(id):
    new_id = int(id) - 1
    this_post = requests.get(f"https://api.npoint.io/ed99320662742443cc5b/{new_id}").json()
    return render_template("post.html", post=this_post)

if __name__ == "__main__":
    app.run(debug=True)