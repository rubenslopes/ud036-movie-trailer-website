class Movie():
    """This class provides a way to store movie related information

    Args:
        movie_title (str): Movie title.
        movie_storyline (str): Short movie's overview.
        poster_image_url (str): Url for the movie's cover.
        youtube_id (str): Trailer's id from YouTube.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
