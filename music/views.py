from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

# Create your views here.
# takes the request from user and gives mostly websites

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))
    #html=''
    #for a in all_albums:
        #url='/music/'+str(a.id)+'/'
        #html += '<a href="'+ url +'">' + a.album_title +'</a><br>' # directing to music/str(q.id)/ on click
    #return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
