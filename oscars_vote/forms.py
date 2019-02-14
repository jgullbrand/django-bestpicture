from django import forms
from .models import MovieChoice
from django.forms import Textarea

class VoteMovie(forms.ModelForm):

	class Meta:
		model = MovieChoice
		fields = ["title", "score", "choice_explanation"]
		labels = {
            'title': 'Movie Title',
            'score': "Score (1 - 10)",
            'choice_explanation': "Why was this your favorite movie?"
        }
		help_texts = {
            'score': "What would you give this movie on a scale from 1 to 10?",
            'choice_explanation': "loved the storyline? The cast of the film was great? ",
        }