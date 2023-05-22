import os

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get("spotify_client_id"),
        client_secret=os.environ.get("spotify_client_secret"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(sp.current_user())

date = ""
input_is_incorrect = True
while input_is_incorrect:
    date = input("Which year would you like to travel? Type the date in this format YYYY-MM-DD:\n")
    data_lst = date.split("-")
    if len(data_lst) == 3:
        if len(data_lst[0]) == 4 and len(data_lst[1]) == 2 and len(data_lst[2]) == 2:
            if 1 <= int(data_lst[1]) <= 12 and 1 <= int(data_lst[2]) <= 31:
                input_is_incorrect = False

    if input_is_incorrect:
        print("Incorrect format, please try again!")

response = requests.get(f"{BILLBOARD_URL}/{date}/")
soup = BeautifulSoup(markup=response.text, parser='html.parser', features="lxml")
song_names_lst = soup.find_all(name="h3",
                               class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font"
                                      "-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal"
                                      "@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

song_names = [x.getText().strip() for x in song_names_lst]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"\"{song}\" doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False,
                                   description="Very good Playlist")

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
