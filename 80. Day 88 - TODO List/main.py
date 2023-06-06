from flask import Flask, render_template
# , redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    is_completed = db.Column(db.Boolean, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
