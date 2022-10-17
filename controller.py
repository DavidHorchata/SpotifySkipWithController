from inputs import get_gamepad
from skipSong import skipSong, incrementVolume
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


class Controller:
    def __init__(self) -> None:
        self.flag = True

    def startLoop(self):

        load_dotenv()

        scope = ['user-read-currently-playing', 'user-modify-playback-state', 'user-read-playback-state']
        username = os.getenv("username")
        client_id = os.getenv("client_id")
        secret = os.getenv("secret")
        device_id = os.getenv("device_id")


        token = SpotifyOAuth(scope=scope, username=username, client_id=client_id, client_secret=secret, redirect_uri='http://127.0.0.1:8080/')
        spotifyObject = spotipy.Spotify(auth_manager= token)

        while self.flag:
            events = get_gamepad()

            for event in events:

                if event.code == 'BTN_TR' and event.state == 1:
                    skipSong(spotifyObject, device_id)

                elif event.code =='BTN_WEST' and event.state == 1:
                    incrementVolume(spotifyObject, device_id)
                else:
                    pass