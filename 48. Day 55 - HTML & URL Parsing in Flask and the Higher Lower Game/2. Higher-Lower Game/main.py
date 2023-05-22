import random

from flask import Flask

app_flask = Flask(__name__)


@app_flask.route("/")
def guess_the_number():
    return "<h1>Guess the number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='count-1-to-10-gif'>"


random_num = random.randint(0, 9)


@app_flask.route("/<int:num>")
def is_num_correct(num):
    if num > random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif num < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app_flask.run(debug=True)
