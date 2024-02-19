from fastapi import FastAPI
import json

from api.config import CLIENT_ID, REDIRECT_URI
from api.controller import Oauth
from api.model import UserData
from api.schema import AuthCode


app = FastAPI()


@app.post("/oauth")
async def oauth_api(data: AuthCode):
    """
    앱으로부터 authorization code를 받은 후 아래 수행:
    1. 전달받은 authorization code를 통해서 access_token, refresh_token을 발급.
    2. access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
    3. 해당 식별 정보를 서비스 DB에 저장 (회원가입)
    3-1. 만약 이미 있을 경우, (3) 과정 스킵
    4. 사용자 식별 id를 바탕으로 서비스 전용 access_token 생성
    """
    code = data.code
    
    oauth = Oauth()
    auth_info = oauth.auth(code)
    user = oauth.userinfo("Bearer " + auth_info['access_token'])

    user = UserData(user)
    user = user.serialize()

    return user


@app.get("/oauth/url")
async def oauth_url_api():
    """
    Kakao OAuth URL 가져오기
    """
    return {
        'kakao_oauth_url': f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code" 
    }