from django.conf.urls import url
from . import views
import datetime as dt

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^pics/$',views.mygallery,name='pics')
]