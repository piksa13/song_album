from django.shortcuts import render
from django.http import HttpResponse
from .models import Album


# Create your views here.
# takes the request from user and gives mostly websites

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
