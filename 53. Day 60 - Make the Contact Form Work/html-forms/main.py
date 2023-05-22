from flask import Flask, render_template, request
import requests
import smtplib

BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"
MY_EMAIL = "hellomy98d@gmail.com"
MY_PASSWORD = "aeyzoterumrnhoux"

app = Flask(__name__)

blogs = requests.get(url=BLOG_API).json()

@app.route("/")
def home():
    p = ['salman', 'haseeb', 'hunain']
    return render_template(template_name_or_list="index.html", blogs=blogs, p=p, h1_data="Salman's Blog")

@app.route("/login", methods = ["POST", "GET"])
def recieve_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Username: {name}, Password: {password}</h1>"

@app.route("/post/<id>")
def click_post(id):
    # id = 0
    id = int(id) - 1
    return render_template(template_name_or_list="current_post.html", blogs=blogs,id=id)

@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html", h1_data="About Me")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        if name != "" and email != "" and phone != "" and message != "":
            email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                print(0)
                connection.starttls()
                print(1)
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="ninjacombo99@gmail.com",
                                    msg=f"Subject:New Message!\n\n{email_message}")
            return render_template(template_name_or_list="contact.html", h1_data=f"Successfully sent your message")
        else:
            return render_template(template_name_or_list="contact.html", h1_data=f"Error Sending Message")
    return render_template(template_name_or_list="contact.html", h1_data="Contact Me")

@app.route("/post")
def post():
    return render_template(template_name_or_list="post.html", h1_data="Sample Post")


if __name__ == "__main__":
    app.run(debug=True)
