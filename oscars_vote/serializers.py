from .models import MovieChoice

from rest_framework import serializers

class MovieDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MovieChoice
		fields = ("title", "score", "choice_explanation")