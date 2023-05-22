from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/robots.txt")
def go_bro():
    return "robots are made"


if __name__ == "__main__":
    app.run()
