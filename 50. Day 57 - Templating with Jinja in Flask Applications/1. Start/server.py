from flask import Flask, render_template
import random
import datetime
import requests

GENDER_API = "https://api.genderize.io?name="
AGE_API = "https://api.agify.io/?name="
BLOGS_API = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(import_name=__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template(template_name_or_list="index.html", num_random=random_number, year=current_year)


@app.route("/guess/<name>")
def guess_name_and_gender(name):
    name = name.title()
    gender = requests.get(url=GENDER_API + name).json()["gender"]
    age = requests.get(url=AGE_API + name).json()["age"]
    return render_template(template_name_or_list="prediction.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def blog(num):
    all_posts = requests.get(url=BLOGS_API).json()
    return render_template(template_name_or_list="blog.html", posts=all_posts, blog_num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
