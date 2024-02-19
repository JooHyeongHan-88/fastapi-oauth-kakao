import streamlit as st

from utils import get_login_url, redirect, post_auth_code


code = st.query_params.get('code')


st.title("FastAPI Kakao OAuth App")
st.subheader("FastAPI를 이용한 Kakao OAuth 연동 로그인 예제입니다.")
st.divider()

if not code:
    if st.button("카카오 로그인"):
        url = get_login_url()
        redirect(url)
else:
    user = post_auth_code(code)

    if type(user) is dict:
        st.write(user["nickname"])
        st.image(user["profile"])

        if st.button("로그아웃"):
            pass
    else:
        st.write(user)