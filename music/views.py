# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Album
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    context ={'all_albums': all_albums}
    return render(request,'music/index.html',context)

def detail(request, album_id):
    return HttpResponse("<h2>Detail for album id "+str(album_id)+"</h2>")


