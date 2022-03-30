import requests
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth

TIMEOUT = 300

SPOTIPY_CLIENT_ID = '06833f31695a4da4acf12d46d15a464b'
SPOTIPY_CLIENT_SECRET = 'b2bb43b6ad6e47c0a1446e1a7c6c3f1d'

scope = "user-library-read user-library-modify"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri='http://0.0.0.0:5000/', scope=scope))
# sp_write = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri='http://0.0.0.0:5000/', scope=write_scope))


# my_tracks = []
# offset = 0

# while True:
# 	playlists = sp_read.current_user_playlists(limit=50, offset=offset)["items"]
# 	if not playlists:
# 		break
# 	offset += 50
# 	for pl in playlists:
# 		tracks = sp_read.playlist(pl["id"], fields=['tracks'])["tracks"]["items"]
# 		my_tracks.extend([t["track"]["id"]for t in tracks])

# my_tracks = list(set(my_tracks))
# print(f"Existed Loop! \n Total no of tracks: {len(my_tracks)}")

# chunk_size = 20
# tracks_not_yet_liked = []
# for i in range(0, len(my_tracks), chunk_size):
# 	chunk = my_tracks[i:i+chunk_size]
# 	track_ids = list(filter(None, chunk))
# 	is_track_liked = sp_read.current_user_saved_tracks_contains(tracks=track_ids)
# 	tracks_not_yet_liked.extend([track for track, is_liked in zip(my_tracks, is_track_liked) if not is_liked])
	
# print(f"Tracks not yet liked: {len(tracks_not_yet_liked)}\n\n{tracks_not_yet_liked}")
# if tracks_not_yet_liked:
# 	sp_write.current_user_saved_tracks_add(tracks=tracks_not_yet_liked)


sp_auth = spotipy.oauth2.SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, proxies=None, requests_timeout=None)
token = sp_auth.get_access_token()

print(f"Token: {token}")

headers = {
	"content-type": "application/json",
    "authentication": f"Bearer {token}"
}

response = requests.get("https://api.spotify.com/v1/me/tracks", headers=headers, timeout=TIMEOUT)

print(response)
