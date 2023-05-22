from flask import Flask, render_template
import requests

BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(import_name=__name__)

blogs = requests.get(url=BLOG_API).json()

@app.route("/")
def home():
    p = ['salman', 'haseeb', 'hunain']
    return render_template(template_name_or_list="index.html", blogs=blogs, p=p)

@app.route("/post/<id>")
def click_post(id):
    # id = 0
    id = int(id) - 1
    return render_template(template_name_or_list="current_post.html", blogs=blogs,id=id)

@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")

@app.route("/contact")
def contact():
    return render_template(template_name_or_list="contact.html")

@app.route("/post")
def post():
    return render_template(template_name_or_list="post.html")


if __name__ == "__main__":
    app.run(debug=True)
