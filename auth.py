import requests
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN_URL

def get_access_token(auth_code):
    params = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code
    }

    response = requests.post(TOKEN_URL, params=params)
    response.raise_for_status()

    return response.json()["access_token"]
