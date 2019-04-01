import requests
import json
import os
from datetime import datetime


class Movie(object):
    '''

    Represents each movie result from Movie DB API

    '''

    def __init__(self, movie_id, title, popularity, release_date, poster_path, overview):
        self.id = movie_id
        self.title = title
        self.popularity = popularity
        self.release_date = release_date
        self.poster_path = poster_path
        self.overview = overview

    def __repr__(self):
        return '<Movie %r %r>' % (self.title, self.release_date)


def popular_movies(page):
    '''
    Fetches popular movies from Movie DB API.

    Args:
        page (int): Page number I want to retrieve from movie API

    Returns:
        list: A list of Movie objects
        int: Total number of pages with results
    '''

    payload = {
        'api_key': 'b597218768d0c72e213e80dc8888266b',
        'page': page
    }

    response = requests.request(
        "GET", 'https://api.themoviedb.org/3/movie/popular', params=payload
    )

    output = json.loads(response.text)
    movies = []
    for film in output['results']:
        movie = Movie(
            movie_id=film['id'],
            title=film['title'],
            popularity=film['popularity'],
            release_date=datetime.strptime(film['release_date'], '%Y-%m-%d'),
            poster_path=film['poster_path'],
            overview=film['overview']
        )

        movies.append(movie)

    return movies, output['total_pages']
