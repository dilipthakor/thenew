# -*- coding: utf-8 -*-
from django.http import HttpResponse
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Dilip Thakor </h1>")
