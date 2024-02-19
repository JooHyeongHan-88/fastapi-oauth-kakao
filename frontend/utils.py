from streamlitextras.webutils import stxs_javascript
import requests
import json

from config import API_URL


def get_login_url() -> str:
    response = requests.get(f"{API_URL}/oauth/url", headers={"Content-Type": "application/json"})
    data = response.json()
    url = data.get('kakao_oauth_url')
    return url


def redirect(url: str):
    stxs_javascript(f"window.location.replace('{url}');")


def post_auth_code(code: str):
    response = requests.post(f"{API_URL}/oauth", json={"code": code})
    
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code