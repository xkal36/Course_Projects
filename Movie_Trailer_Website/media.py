import webbrowser

class Movie():
    """
    This class provides a way to store movie related information
    
    Attributes:
        movie_title (str): The title of the movie
        movie_storyline (str): The storyline of the movie
        poster_image (str): The url of the poster image of the movie
        youtube_trailer (str): The url of the youtube trailer of the movie
        imdb_rating (int): Movie rating from imdb.com
	"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating

    # opens the youtube trailer in the page when when the tile is clicked
    def show_movie_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)