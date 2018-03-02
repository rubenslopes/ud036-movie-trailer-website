import fresh_tomatoes
import json
import media
import urllib


API_KEY = ''


def get_youtube_trailer(movie_id):
    """Retrive the first YouTube trailer, if there is one"""

    conn = urllib.urlopen('https://api.themoviedb.org/3/movie/%s/videos?api_key=%s' % (movie_id, API_KEY))
    videos = json.loads(conn.read())

    for v in videos['results']:
        if v['type'] == 'Trailer' and v['site'] == 'YouTube':
            return v['key']
    
    return None


def main():
    """Retrive a list of upcoming movies"""

    connection = urllib.urlopen('https://api.themoviedb.org/3/movie/upcoming?api_key=%s' % API_KEY)
    movies_json = json.loads(connection.read())

    movies = []

    for m in movies_json['results']:
        trailer = get_youtube_trailer(m['id'])
        img = 'https://image.tmdb.org/t/p/w500/%s' % m['poster_path']
        movies.append(media.Movie(m['title'], m['overview'], img, trailer))

    fresh_tomatoes.open_movies_page(movies)


main()