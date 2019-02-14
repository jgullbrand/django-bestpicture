from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VoteMovie
from .models import MovieChoice
from django.db.models import Avg

def index(request):
	if request.method == "POST":
		movie_form = VoteMovie(request.POST)
		if movie_form.is_valid():
			movie_form.save()
			title = movie_form.cleaned_data.get("title")
			messages.success(request, f'You have successfully voted for {title}!')
			return redirect("index")
	else:
		movie_form = VoteMovie()	

	bp_result = MovieChoice.objects.filter(title='Black Panther').count()
	bp_avg = round(MovieChoice.objects.filter(title='Black Panther').aggregate(avg=Avg('score'))['avg'],1)
	bklan_result = MovieChoice.objects.filter(title='BlacKkKlansman').count()
	bklan_avg = round(MovieChoice.objects.filter(title='BlacKkKlansman').aggregate(avg=Avg('score'))['avg'],1)
	brhapsody_result = MovieChoice.objects.filter(title='Bohemian Rhapsody').count()
	brhapsody_avg = round(MovieChoice.objects.filter(title='Bohemian Rhapsody').aggregate(avg=Avg('score'))['avg'],1)
	fav_result = MovieChoice.objects.filter(title='The Favourite').count()
	fav_avg = round(MovieChoice.objects.filter(title='The Favourite').aggregate(avg=Avg('score'))['avg'],1)
	gbook_result = MovieChoice.objects.filter(title='Green Book').count()
	gbook_avg = round(MovieChoice.objects.filter(title='Green Book').aggregate(avg=Avg('score'))['avg'],1)
	starborn_result = MovieChoice.objects.filter(title='A Star Is Born').count()
	starborn_avg = round(MovieChoice.objects.filter(title='A Star Is Born').aggregate(avg=Avg('score'))['avg'],1)
	vice_result = MovieChoice.objects.filter(title='Vice').count()
	vice_avg = round(MovieChoice.objects.filter(title='Vice').aggregate(avg=Avg('score'))['avg'],1)
	roma_result = MovieChoice.objects.filter(title='Roma').count()
	roma_avg = round(MovieChoice.objects.filter(title='Roma').aggregate(avg=Avg('score'))['avg'],1)

	context = {
		"movie_form": movie_form, 
		"bp_result": bp_result,
		"bp_avg": bp_avg,
		"bklan_result": bklan_result,
		"bklan_avg": bklan_avg,
		"brhapsody_result": brhapsody_result,
		"brhapsody_avg": brhapsody_avg,
		"fav_result": fav_result,
		"fav_avg": fav_avg,
		"gbook_result": gbook_result,
		"gbook_avg": gbook_avg,
		"starborn_result": starborn_result,
		"starborn_avg": starborn_avg,
		"vice_result": vice_result,
		"vice_avg": vice_avg,
		"roma_result": roma_result,
		"roma_avg": roma_avg,
	}
	return render(request, "oscars_vote/index.html", context)

def results(request):

	context = {}
	return render(request, "oscars_vote/results.html", context)