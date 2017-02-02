from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Album
from django.http import Http404

# Create your views here.
# takes the request from user and gives mostly websites

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' :album })
