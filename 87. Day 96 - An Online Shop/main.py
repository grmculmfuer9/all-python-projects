import bcrypt
import stripe
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists
import os

import sys


def set_certificate(certificate_path: str) -> None:
    stripe.ca_bundle_path = certificate_path


SECRET_KEY = '09dkdklJ3DIl2)@#kdjlk5PsoI#OJKLkd6kfl23ioA2@BXfls3i'

# pw = b"skU229!oMpa@pA3"
#
# #hash a pw for the first time with randomly generated salt
# hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
#
# # Check that an unhashed password matches one that has previously been hashed
# if bcrypt.checkpw(pw, hashed):
#     print("It matches!")
# else:
#     print("It does not match >:(")

planet_price_dict = {
    'mercury': {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Mercury',
                },
            'unit_amount': 1000000,
            },
            'quantity': 1,
            },
    'venus': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Venus',
                    },
                'unit_amount': 3000000,
                },
                'quantity': 1,
                },
    'earth': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Earth',
                    },
                'unit_amount': 77777777,
                },
                'quantity': 1,
                },
    'mars': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Mars',
                    },
                'unit_amount': 5000000,
                },
                'quantity': 1,
                },
    'jupiter': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Jupiter',
                    },
                'unit_amount': 50000000,
                },
                'quantity': 1,
                },
    'saturn': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Saturn',
                    },
                'unit_amount': 50000000,
                },
                'quantity': 1,
                },
    'uranus': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Uranus',
                    },
                'unit_amount': 4206900,
                },
                'quantity': 1,
                },
    'neptune': {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Neptune',
                    },
                'unit_amount': 900100,
                },
                'quantity': 1,
                },
    'pluto': {
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': 'Pluto',
            },
            'unit_amount': 999999999999999,
        },
        'quantity': 1,
    },
}

base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

print('before', stripe.ca_bundle_path)
set_certificate(f"{base_path}/stripe/data/ca-certificates.crt")
print()
print('after', stripe.ca_bundle_path)

# Set the template and static directories relative to the base path
template_dir = os.path.join(base_path, 'templates')
static_dir = os.path.join(base_path, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

path_to_sql_file = os.path.join(base_path, 'instance/db.sqlite3')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path_to_sql_file}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    logged_in = db.Column(db.Integer)


# # Initialize database
try:
    if open(os.path.join('instance/db.sqlite3')):
        pass
except FileNotFoundError:
    with app.app_context():
        db.create_all()
        


@app.route('/')
def home():
    logged_in = db.session.query(exists().where(User.logged_in == 1)).scalar()
    # button = True
    if logged_in:
        button = True
        print(logged_in)
        return render_template('index.html', logoutbtn=button)
    else:
        print("false", logged_in)
        button = False
        return render_template('index.html', logoutbtn=button)


# This is your test secret API key.
stripe.api_key = 'sk_test_51NHaRLF4Ntyyg1eLuXIFtggwYy235YCGFJ5Hh6x6UhW8DnqnXcuJU7JFZC6kflYwI3eJjC8wdEnWdBipl4kr' \
                 'Sm3300DWAyXT9d'

YOUR_DOMAIN = 'http://127.0.0.1:5000'


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    checkout_session = ''
    os.environ['REQUESTS_CA_BUNDLE'] = 'https://github.com/stripe/stripe-php/blob/master/data/ca-certificates.crt'
    if request.method == 'POST':
        planet = request.form.get('name')
        checkout_session = stripe.checkout.Session.create(
            line_items=[planet_price_dict[planet]],
            mode='payment',
            success_url='http://127.0.0.1:5000//success',
            cancel_url='http://127.0.0.1:5000//cancel'
        )

    return redirect(checkout_session.url, code=303)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/cancel')
def cancel():
    return render_template('cancel.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('_flashes', None)
    error = None
    if request.method == 'POST':
        email = request.form.get("email")
        pw = request.form.get('password')
        eq = db.session.query(exists().where(User.email == email)).scalar()
        id = db.session.query(User.id).filter_by(email=email).scalar()
        if eq:
            print("email exists, id is", id)
            hashed = db.session.query(User.password).filter_by(id=1).scalar()
            encoded_pw = bytes(pw, 'UTF-8')
            check = bcrypt.checkpw(encoded_pw, hashed)
            if check:
                flash('You are now Logged In')
                user = User.query.filter_by(email=email).first()
                user.logged_in = 1
                db.session.commit()
                return redirect(url_for('home'))
            else:
                print("That password is incorrect", check)
                return render_template('login.html', error=error)
        else:
            print('That email is not in our system')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
def logout():
    user = User.query.filter_by(logged_in=1).first()
    user.logged_in = 0
    db.session.commit()
    flash("You are now logged out")
    return redirect(url_for('home'))


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        pw = request.form.get('password')
        re_pw = request.form.get('re-entered-pw')
        email = request.form.get('email')
        if pw == re_pw:
            pw_to_bytes = bytes(pw, 'UTF-8')
        else:
            flash("Sorry, your passwords didn't match")
            redirect(url_for('add_user'))
        hash = bcrypt.hashpw(pw_to_bytes, bcrypt.gensalt())
        new_user = User(
            password=hash,
            email=email
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create_user.html')


if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
