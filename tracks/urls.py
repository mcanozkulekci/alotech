# tracks/urls.py

from django.urls import path
from .views import get_random_artist,index



app_name = 'tracks'

urlpatterns = [
    path('', index, name='index'),

    path('/tracks/<str:genre>/', get_random_artist, name='get_random_artist'),


    #tracks/rap
    #tracks/rock
]