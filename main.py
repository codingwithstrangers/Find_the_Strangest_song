import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID= os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET= os.environ["SPOTIFY_CLIENT_SECRET"]
grant_type = 'client_credentials'

# CLIENT_ID = 'yourid'
# CLIENT_SECRET = 'yoursecret'

url = 'https://accounts.spotify.com/api/token'

response = requests.post(url, {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'client_credentials'
})

data = response.json()
access_token = data['access_token']

print(access_token)

