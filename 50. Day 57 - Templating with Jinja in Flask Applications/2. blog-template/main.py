from flask import Flask, render_template
import requests

BLOGS_API = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/post/<id>")
def show_post(id):
    id = int(id) - 1
    blog_data = requests.get(url=BLOGS_API).json()[id]
    return render_template(template_name_or_list="post.html", data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
