import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os


os.environ['SPOTIPY_CLIENT_ID'] = 'NEVER PUSH KEYS TO GITHUB'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'NEVER PUSH KEYS TO GITHUB'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://URL HERE/'

def convert_ms(millis):
    minutes, remainder = divmod(millis, 1000 * 60)
    seconds = remainder // 1000

    return {"minutes": minutes, "seconds": seconds}


def percentage(grundwert: int, anteil: int):
    return round(anteil / grundwert * 100)


class Spotify():
    def __init__(self):
        self.__scope = """user-library-read user-read-currently-playing user-read-playback-state streaming 
        playlist-read-collaborative user-read-private user-read-email playlist-read-private 
        user-read-playback-position user-library-modify """
        self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.__scope))

    def get_data(self):

        currently_playing = self.__sp.currently_playing()

        if currently_playing:
            name = currently_playing["item"]["name"]
            progress = currently_playing["progress_ms"]
            is_playing = currently_playing["is_playing"]
            duration = currently_playing["item"]["duration_ms"]
            image = currently_playing["item"]["album"]["images"][1]["url"]
            progress_percent = percentage(duration, progress)
            artists = []
            album_name = currently_playing["item"]["album"]["name"]
            for artist in currently_playing["item"]["artists"]:
                artists.append(artist["name"])

            devices = self.__sp.devices()["devices"]
            currently_playing_device = ""

            for device in devices:
                if device["is_active"]:
                    currently_playing_device = device["name"]

            data = {"name": name,
                    "progress": convert_ms(progress),
                    "is_playing": is_playing,
                    "duration": convert_ms(duration),
                    "image": image,
                    "artist": artists,
                    "device": currently_playing_device,
                    "progress_percentage": progress_percent,
                    "album_name":album_name}
            return data
        else:
            print("No data from Spotify!")


if __name__ == "__main__":
    spotify = Spotify()
    data = spotify.get_data()
    for d in data:
        print(d," : ", data[d])
