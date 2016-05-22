import webbrowser

class Flix():
    RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, storyline, poster_image, genre,youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
class Movie(Flix):

    def __init__(self, title, storyline, poster_image, genre, youtube_trailer, duration, director, year):
        Flix.__init__(self, title, storyline, poster_image, genre, youtube_trailer)
        self.duration = duration
        self.director = director
        self.year = year

        
class Anime(Flix):

    def __init__(self, title, storyline, poster_image, genre, youtube_trailer, total_episodes, producer, year):
        Flix.__init__(self, title, storyline, poster_image, genre, youtube_trailer)
        self.episodes = total_episodes
        self.producer = producer
        self.year = year
