from flask import Flask, render_template, request
from movie_db_api import popular_movies

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    movies, pages = popular_movies(page)
    return render_template('home.html', movies=movies, pages=pages, current_page=page)


if __name__ == '__main__':
    app.run(debug=True)
