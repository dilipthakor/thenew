# -*- coding: utf-8 -*-
from django.http import HttpResponse
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Dilip Thakor </h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Detail for album id "+str(album_id)+"</h2>")


