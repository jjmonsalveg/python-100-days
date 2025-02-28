import os

import spotipy
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
authorize_url = auth_manager.get_authorize_url()
print(f"Paste this url in your browser: {authorize_url} \n")

redirected_url = input("Enter the URL you were redirected to after agree: ")
auth_code = redirected_url.split("?code=")[1].split("&")[0]

token_info = auth_manager.get_access_token(auth_code)

with open("token.txt", "w") as file:
    file.write(str(token_info).replace("'", '"'))

print("Access Token:", token_info["access_token"])
