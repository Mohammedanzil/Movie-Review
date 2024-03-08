from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('profile',views.profile,name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_movie',views.add_movie,name='add_movie'),
    path('add_review/<slug:movie_slug>/', views.add_review, name='add_review'),
    path('<str:genre_slug>/<str:movie_slug>/', views.movie_reviews, name='movie_reviews'),
    path('delete_movie/<str:genre_slug>/<slug:movie_slug>/', views.delete_movie, name='delete_movie'),

]