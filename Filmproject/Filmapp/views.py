from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie,Genre
from django.contrib.auth.decorators import login_required


# Create your views here.
# def index(request):
#     return HttpResponse('helo')

@login_required(login_url='user/login')
def allFilms(request,g_slug=None):
    g_page=None
    films_list=None
    if g_slug!=None:
        g_page=get_object_or_404(Genre,slug=g_slug)
        films_list=Movie.objects.all().filter(genre=g_page)
    else:
        films_list=Movie.objects.all().filter()
    paginator = Paginator(films_list, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        films = paginator.page(page)
    except (EmptyPage, InvalidPage):
        films = paginator.page(paginator.num_pages)
    return render(request,"genre.html",{'genre':g_page,'films':films})

def filmInfo(request,g_slug,f_slug):
    try:
        movie=Movie.objects.get(genre__slug=g_slug,slug=f_slug)
    except Exception as e:
        raise e
    return render(request,'info.html',{'movie':movie})