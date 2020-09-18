import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Movies.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Movie(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.form:
        movie = Movie(title=request.form.get("title"))
        db.session.add(movie)
        db.session.commit()
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)

@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    movie = Movie.query.filter_by(title=oldtitle).first()
    movie.title = newtitle
    db.session.commit()
    return redirect("/")    

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    movie = Movie.query.filter_by(title=title).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)