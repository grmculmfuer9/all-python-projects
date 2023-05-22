from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(template_name_or_list="index.html")


@app.route("/profile")
def salman_profile():
    return render_template(template_name_or_list="salman.html")


if __name__ == "__main__":
    app.run(debug=True)
