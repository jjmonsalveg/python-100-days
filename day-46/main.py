import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(
    scope=scope,
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri=spotify_redirect_uri,
    show_dialog=True,
    cache_path="token.txt",
)
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]
print("User ID:", user_id)


day_in_time = input(
    "Wich year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
base_billboard_url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(base_billboard_url + day_in_time, headers=header)

response.raise_for_status()
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
song_names_spans = soup.select("li ul li h3")
by_spans = soup.select("li ul li span")
song_names = [song.getText().strip() for song in song_names_spans]

spotify_data = []
for i in range(len(song_names)):
    song_name = song_names[i]
    result = sp.search(
        q=f"track:{song_name} year:{day_in_time.split('-')[0]}", type="track"
    )
    try:
        uri = result["tracks"]["items"][0]["uri"]
        spotify_data.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")
        continue

    print(f"{i}. {song_name} - url spotify: {uri}")

playlist_id = sp.user_playlist_create(
    user=user_id, name=f"{day_in_time} Billboard 100", public=False
)

sp.playlist_add_items(playlist_id["id"], spotify_data)
