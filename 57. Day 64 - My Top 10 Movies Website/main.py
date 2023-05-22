from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import requests

TMDB_API_URL = "https://api.themoviedb.org/3/search/movie?api_key=ff857a5ae82c61d77fa9785e9c505898&language=en-US&page=1&include_adult=false&query="

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(2500), nullable=False)
    img_url = db.Column(db.String(400), nullable=False)
    homepage_url = db.Column(db.String(400), nullable=False)


class MovieForm(FlaskForm):
    rating = StringField(label="Rating", validators=[DataRequired()])
    review = StringField(label="Review", validators=[DataRequired()])
    submit = SubmitField(label="Update")


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


with app.app_context():
    db.create_all()

    # ADDED THIS DATA IN THE FIRST RUN
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
    #                 "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to "
    #                 "a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )

    # db.session.add(new_movie)
    # db.session.commit()
    # END OF THE DATA


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    print(request.method)
    id = request.args.get('id')
    movie_selected = Movie.query.get(id)
    movie_form = MovieForm()
    if request.method == "POST":
        movie_selected.rating = movie_form.rating.data
        if "\"" in movie_form.review.data:
            movie_selected.review = movie_form.review.data.replace("\"", "")
        movie_selected.review = movie_form.review.data
        db.session.commit()
        print(movie_form.rating.data)
        print(movie_form.review.data)
        # print(request.form["rating"])
        return redirect(url_for(endpoint="home"))
    return render_template(template_name_or_list="edit.html", movie=movie_selected, movie_form=movie_form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    id = request.args.get('id')
    movie_selected = Movie.query.get(id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_movie = AddMovie()
    if request.method == "POST":
        tmdb_url = TMDB_API_URL + add_movie.title.data + "#"
        movies_data = requests.get(url=tmdb_url).json()["results"]
        return render_template(template_name_or_list="select.html", movies=movies_data)
    return render_template(template_name_or_list="add.html", add_movie=add_movie)


@app.route("/select", methods=["GET", "POST"])
def select():
    # Dump data in dump.txt
    movie = eval(request.args.get(key="movie"))
    id = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key=ff857a5ae82c61d77fa9785e9c505898&language=en-US")
    url = id.json()["homepage"]
    print('ur', url)
    new_movie = Movie(title=movie["title"], year=movie["release_date"], description=movie["overview"],
                      rating=0, review="Getting", ranking="N/A",
                      img_url=f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}",
                      homepage_url=url)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for(endpoint="edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
