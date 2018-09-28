from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from django.db import models
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def mygallery(request):
    date = dt.date.today()
    photos = Image.get_all()
    return render(request, 'all-pics/myhomepics.html', {"date": date, "photos":photos})

