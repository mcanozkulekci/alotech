from django.shortcuts import render

# Create your views here.

import json
import random
from django.http import JsonResponse

def get_random_artist(request, genre):
    # Load the genres data from the JSON file
    with open('alotech/genres.json') as file:
        genres = json.load(file)

    # Retrieve the list of artists for the given genre
    genre_artists = genres.get(genre, [])

    # Pick a random artist from the list
    random_artist = random.choice(genre_artists) if genre_artists else None

    response_data = {
        'genre': genre,
        'artist': random_artist
    }

    return JsonResponse(response_data)

    