from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///anime.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    favourite_C = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    # READ ALL RECORDS
    all_anime = db.session.query(Anime).all()
    return render_template("index.html", animes=all_anime)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_anime = Anime(
            title=request.form["title"],
            favourite_C=request.form["FC"],
            rating=request.form["rating"]
        )
        db.session.add(new_anime)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        anime_id = request.form["id"]
        anime_to_update = Anime.query.get(anime_id)
        anime_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    anime_id = request.args.get('id')
    anime_selected = Anime.query.get(anime_id)
    return render_template("edit_rating.html", anime=anime_selected)


@app.route("/edit_favourite_character", methods=["GET", "POST"])
def edit_fc():
    if request.method == "POST":
        # UPDATE RECORD
        anime_id = request.form["id"]
        anime_to_update = Anime.query.get(anime_id)
        anime_to_update.favourite_C = request.form["favourite_C"]
        db.session.commit()
        return redirect(url_for('home'))
    anime_id = request.args.get('id')
    anime_selected = Anime.query.get(anime_id)
    return render_template("edit_favourite_character.html", anime=anime_selected)


@app.route("/delete")
def delete():
    anime_id = request.args.get('id')

    # DELETE A RECORD BY ID
    anime_to_delete = Anime.query.get(anime_id)
    db.session.delete(anime_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

