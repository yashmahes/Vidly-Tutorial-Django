from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie, Genre


def index(request):
    # movies = Movie.objects.all()
    # movies = Movie.objects.filter(release_year=1984)
    # movies = Movie.objects.get(id=1)

    data = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])

    # return HttpResponse(output)

    return render(request, 'movies/index.html', {'data': data})


def detail(request, movie_id):
    # data = Movie.objects.get(id=movie_id)
    data = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'data': data})


def home(request):
    return render(request, 'home.html')
