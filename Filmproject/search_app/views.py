from django.shortcuts import render
from Filmapp.models import Movie
from django.db.models import Q
# Create your views here.


def SearchResult(request):
    film=None
    query=None
    if 'q' in request.GET:
        query= request.GET.get('q')
        films=Movie.objects.all().filter(Q(title__contains=query) | Q(actors__contains=query))
        return render(request,'search.html',{'query':query,'films':films})