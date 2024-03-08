import uuid

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering=('title',)
        verbose_name='genre'
        verbose_name_plural='genres'

    def get_url(self):
        return reverse('Filmapp:films_by_genre',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.title)
class Movie(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    poster = models.ImageField(upload_to='posters',blank=True)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=200, default='Unknown')
    trailer_link = models.URLField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,default=1)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('Filmapp:filmInfo', args=[self.genre.slug,self.slug])

    class Meta:
        ordering=('title',)
        verbose_name='film'
        verbose_name_plural='films'

    def __str__(self):
        return '{}'.format(self.title)

class Review(models.Model):
    title = models.ForeignKey('Filmapp.Movie', on_delete=models.CASCADE, related_name='filmapp_reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    review_text = models.TextField(max_length=500)
    slug = models.SlugField(max_length=250, unique=True, default=uuid.uuid4)
    rating = models.IntegerField()

    class Meta:
        ordering = ('review_text',)
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return '{}'.format(self.review_text)