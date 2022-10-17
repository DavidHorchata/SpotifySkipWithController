
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os






scope = ['user-read-currently-playing', 'user-modify-playback-state', 'user-read-playback-state']
token = SpotifyOAuth(scope=scope)