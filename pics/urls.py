from django.conf.urls import url
from . import views
import datetime as dt

urlpatterns=[
    
    url('',views.mygallery,name='pics')
]