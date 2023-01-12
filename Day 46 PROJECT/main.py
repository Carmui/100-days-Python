from bs4 import BeautifulSoup
import requests
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scrapping 100 Bilboards
#question = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
question = "2000-08-12"

page = ''
while page == '':
    try:
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{question}/")
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue

soup = BeautifulSoup(response.text, 'html.parser')
song_names_list = soup.find_all(name="h3", class_="a-no-trucate")

song_names = [song.getText().strip() for song in song_names_list]


# Spotify Authentication
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                    scope=scope,
                                    client_id="YOUR_CLIENT_ID",
                                    client_secret="YOUR_CLIENT_SECRET",
                                    redirect_uri="http://example.com",
                                    cache_path="token.txt",
                                    show_dialog=True)
)

user_id = sp.current_user()["id"]

# Searching through Spotify

songs_uris = []
year = question.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print("Song doesn't exists, skipping.")


playlist = sp.user_playlist_create(user_id, name=f"{question} Billboard100", public=False)
#print(playlist["id"])
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)

