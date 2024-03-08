from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.

from .models import Genre,Review,Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Genre,GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','release_date','description','actors','trailer_link','genre','poster']
    list_editable = ['actors','description','genre','poster']
    prepopulated_fields = {'slug':('title',)}
    list_per_page = 15
admin.site.register(Movie,MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title','review_text','rating']
    list_editable = ['review_text']
    prepopulated_fields = {'slug':('review_text',)}
    list_per_page = 15
admin.site.register(Review,ReviewAdmin)