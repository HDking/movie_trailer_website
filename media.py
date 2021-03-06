import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	"""constructor for the Movie class takes 4 attributes"""
	def __init__(self, movie_title, movie_storyline,poster_image, trailer_youtube, main_actor):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.main_actor = main_actor

	"""opens the URL for the Youtube trailer"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


