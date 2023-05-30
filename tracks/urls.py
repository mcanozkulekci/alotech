from django.urls import path

from . import views


app_name= 'tracks'
urlpatterns = [

    path('<str:genre>/', views.get_random_artist, name='get_random_artist'),
    

]
