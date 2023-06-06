from flask import Flask, render_template, request, abort, redirect, url_for, flash
# , redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    todos = relationship('TodoList')


class TodoList(db.Model):
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    is_completed = db.Column(db.Boolean, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    todo_author = relationship("User", back_populates="todos")


# with app.app_context():
#     db.create_all()


@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    return User.query.get(int(user_id))


@app.route('/')
def home():
    if current_user.is_authenticated:
        all_items = TodoList.query.filter_by(author_id=current_user.id).all()
        # all_items = TodoList.query.all()
        count = len(all_items)
        print(count)
        print(current_user.id)
    else:
        count = 0
        all_items = []
        flash('Please login to add tasks')
    return render_template('index.html', all_items=all_items, count=count, has_logged_in=current_user.is_authenticated)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':
        task = request.form['task']
        is_task_present = TodoList.query.filter_by(task=task).first()
        if is_task_present != None:
            message = f'{task} task already present'
            flash(message)
            return redirect(url_for('home'))
        elif task == "":
            message = 'Empty task cannot be added'
            flash(message)
            return redirect(url_for('home'))
        new_task = TodoList(task=task, is_completed=False, author_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return abort(404)


@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
# @login_required
def complete_item(item_id):
    item = TodoList.query.get(item_id)
    if request.method == 'POST':
        print(item_id)
        db.session.delete(item)
        db.session.commit()
        print('here')
        return redirect(url_for('home'))
    return abort(404)


@app.route('/newlist', methods=['GET', 'POST'])
@login_required
def new_list():
    # if request.method == 'POST':
    all_items = TodoList.query.filter_by(author_id=current_user.id).all()
    for item in all_items:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('home'))
    # return abort(404)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user == None:
            message = 'Email not registered'
            flash(message)
            return redirect(url_for('login'))
        elif password != user.password:
            message = 'Incorrect password'
            flash(message)
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', has_logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user != None:
            message = 'Email already registered'
            flash(message)
            return redirect(url_for('register'))
        elif password == "":
            message = 'Password cannot be empty'
            flash(message)
            return redirect(url_for('register'))
        else:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', has_logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
