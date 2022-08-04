import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


def skipSong():

    load_dotenv()


    scope = ['user-read-currently-playing', 'user-modify-playback-state', 'user-read-playback-state']
    username = os.getenv("username")
    client_id = os.getenv("client_id")
    secret = os.getenv("secret")
    device_id = os.getenv("device_id")


    token = SpotifyOAuth(scope=scope, username=username, client_id=client_id, client_secret=secret, redirect_uri='http://127.0.0.1:8080/')
    spotifyObject = spotipy.Spotify(auth_manager= token)

    current = spotifyObject.current_playback()
    if not current:

        spotifyObject.start_playback(device_id=device_id)

    spotifyObject.next_track(device_id=device_id)

