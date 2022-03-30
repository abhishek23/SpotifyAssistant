import requests
import urllib
import base64


SPOTIPY_CLIENT_ID = '06833f31695a4da4acf12d46d15a464b'
SPOTIPY_CLIENT_SECRET = 'b2bb43b6ad6e47c0a1446e1a7c6c3f1d'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

TIMEOUT = 300

scope = "user-library-read user-library-modify"
redirect_uri='http://0.0.0.0:5000/'


# Authorization
params = {
    "response_type": "code",
    "client_id": SPOTIPY_CLIENT_ID,
    "scope": scope,
    "redirect_uri": redirect_uri
}
# qs = urllib.parse.urlencode(params)
headers = {
    "Content-Type": "application/json"
}
url = "https://accounts.spotify.com/authorize"
print(url)
auth_response = requests.get("https://accounts.spotify.com/authorize?response_type=code&client_id=06833f31695a4da4acf12d46d15a464b&scope=user-library-read+user-library-modify&redirect_uri=http%3A%2F%2F0.0.0.0%3A5000%2F",
	timeout=TIMEOUT)

print(auth_response.data)


auth_header = base64.urlsafe_b64encode((SPOTIPY_CLIENT_ID + ':' + SPOTIPY_CLIENT_SECRET).encode('ascii'))
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic %s' % auth_header.decode('ascii')
}

payload = {
    'grant_type': 'authorization_code',
    'code': auth_response,
    'redirect_uri': redirect_uri,
    #'client_id': CLIENT_ID,
    #'client_secret': CLIENT_SECRET,
}

# Make a request to the /token endpoint to get an access token
access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)

# convert the response to JSON
access_token_response_data = access_token_request.json()

print(access_token_response_data)