import webbrowser
##import video
class Movie():
    def __init__(self, movie_title, duration,movie_storyline, poster_image, trailer_youtube):
        #video.Video1.__init__(self, movie_title, duration)
        self.title = movie_title
        self.duration= duration
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
