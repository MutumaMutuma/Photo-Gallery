from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from django.db import models
from .models import Image

# Create your views here.

def mygallery(request):
    date = dt.date.today()
    photos = Image.get_all()
    return render(request, 'all-pics/home.html', {"date": date, "photos":photos})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categorys = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"categorys": searched_categorys})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})
