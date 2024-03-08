
from django.urls import path
from . import views
app_name='Filmapp'
urlpatterns = [
    path('', views.allFilms,name='allFilms'),
    path('<slug:g_slug>/',views.allFilms,name='films_by_genre'),
    path('<slug:g_slug>/<slug:f_slug>/', views.filmInfo, name='filmInfo'),
    path('<str:genre_slug>/<str:movie_slug>/', views.filmInfo, name='filmInfo'),
]