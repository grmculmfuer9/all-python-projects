from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f"<strong>{function()}</strong>"

    return bold


def make_italic(function):
    def italic():
        return f"<em>{function()}</em>"

    return italic


def make_underline(function):
    def underline():
        return f"<u>{function()}</u>"

    return underline


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center": center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/11kXFNRcZBFgwo/giphy.gif" alt="kitten-gif">'


@app.route("/robots.txt")
@make_bold
@make_italic
@make_underline
def go_bro():
    return "robots are made"


@app.route("/<path:name>/<int:num>")
def greet(name, num):
    return f"Hello {name}, and {num} years old."


if __name__ == "__main__":
    app.run(debug=True)
