from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MovieChoice (models.Model):
	MOVIE_OPTIONS = (
		("Black Panther", "Black Panther"),
		("BlacKkKlansman", "BlacKkKlansman"),
		("Bohemian Rhapsody", "Bohemian Rhapsody"),
		("The Favourite", "The Favourite"),
		("Green Book", "Green Book"),
		("Roma", "Roma"),
		("A Star Is Born", "A Star Is Born"),
		("Vice", "Vice"),
	)
	title = models.CharField(max_length = 50, choices = MOVIE_OPTIONS)
	score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
	choice_explanation = models.CharField(max_length = 50, blank=True)
	post_date = models.DateTimeField(auto_now_add=True)

	def __str__ (self):
		return f'Movie: {self.title}, Score: {self.score}'



