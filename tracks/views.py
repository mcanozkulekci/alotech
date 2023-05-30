from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

import json
import random
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponse, JsonResponse
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_random_artist(request, genre):
    # Load the genres data from the JSON file
    with open('alotech/genres.json') as file:
        genres = json.load(file)

    # Retrieve the list of artists for the given genre
    genre_artists = genres.get(genre, [])

    # Pick a random artist from the list
    random_artist = random.choice(genre_artists) if genre_artists else None


    if random_artist:
        # Initialize the Spotify API client
        client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Search for the artist on Spotify
        results = spotify.search(q=random_artist, type='artist', limit=1)
        artists = results['artists']['items']

        if artists:
            artist = artists[0]
            artist_id = artist['id']

            # Get the artist's top tracks
            top_tracks = spotify.artist_top_tracks(artist_id=artist_id, country='US')

            # Filter the most popular 10 tracks
            popular_tracks = top_tracks['tracks'][:10]

            # Prepare the response data
            response_data = {
                'genre':genre,
                'tracks': []
            }

            for track in popular_tracks:
                track_info = {
                    'name': track['name'],
                    'album': track['album']['name'],
                    'preview_url': track['preview_url'],
                    'image_url': track['album']['images'][0]['url']
                }
                response_data['tracks'].append(track_info)

        return render(request,"tracklist.html",response_data)
     

    return JsonResponse({'error': 'No artist found for the given genre.'})



def index(request): 
    return render(request,'index.html')