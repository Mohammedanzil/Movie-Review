from . models import Genre
def menu_links(request):
    links=Genre.objects.all()
    return dict(links=links)