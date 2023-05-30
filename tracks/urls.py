# tracks/urls.py

from django.urls import path
from .views import get_random_artist

app_name = 'tracks'

urlpatterns = [
    path('<str:genre>/', get_random_artist, name='get_random_artist'),


    #tracks/rap
    #tracks/rock
]