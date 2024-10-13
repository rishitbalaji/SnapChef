import streamlit as st
import os
from authlib.integrations.requests_client import OAuth2Session
from starlette.config import Config
import requests
from urllib.parse import urlencode

from custom_pages.home import home_page
from custom_pages.about import about_page
from custom_pages.snap import snap_page
from custom_pages.recipe import recipe_page
from custom_pages.meal import meal_page

config = Config(".env")
AUTH0_CLIENT_ID = config("AUTH0_CLIENT_ID", cast=str, default="4wo2govtmyk6dzd7Y9x5Tnph5F9X6oNw")
AUTH0_CLIENT_SECRET = config("AUTH0_CLIENT_SECRET", cast=str, default="k-tGnJ4IwUTC0ngivw4oGxzDe3XgOVffES0WnBJzABDpSmONh2BKWFTs7tRVMVBU")
AUTH0_DOMAIN = config("AUTH0_DOMAIN", cast=str, default="dev-6nmrrzzctnoemwxf.us.auth0.com")

REPLIT_URL = "https://ace3826b-16a3-4a25-ab03-a30945709ba3-00-2a24xan7pdg1o.janeway.replit.dev"
AUTH0_CALLBACK_URL = f"{REPLIT_URL}/"

auth0_base_url = f"https://{AUTH0_DOMAIN}"
auth0_authorize_url = f"{auth0_base_url}/authorize"
auth0_token_url = f"{auth0_base_url}/oauth/token"

if 'auth0_state' not in st.session_state:
    st.session_state.auth0_state = None
if 'auth0_user' not in st.session_state:
    st.session_state.auth0_user = None

def login():
    oauth = OAuth2Session(
        AUTH0_CLIENT_ID,
        AUTH0_CLIENT_SECRET,
        scope='openid profile email',
        redirect_uri=AUTH0_CALLBACK_URL
    )
    try:
        auth_url, state = oauth.create_authorization_url(auth0_authorize_url)
        st.session_state.auth0_state = state
        st.markdown(f'<a href="{auth_url}" target="_self">Login with Auth0</a>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred during login: {str(e)}")

def callback():
    try:
        params = st.query_params
        oauth = OAuth2Session(
            AUTH0_CLIENT_ID,
            AUTH0_CLIENT_SECRET,
            state=st.session_state.auth0_state,
            redirect_uri=AUTH0_CALLBACK_URL
        )
        full_url = f"{AUTH0_CALLBACK_URL}?{urlencode(params)}"
        token = oauth.fetch_token(
            auth0_token_url,
            authorization_response=full_url,
            client_secret=AUTH0_CLIENT_SECRET
        )
        st.session_state.auth0_user = token
        userinfo_response = requests.get(f"{auth0_base_url}/userinfo", headers={
            'Authorization': f'Bearer {token["access_token"]}'
        })
        userinfo = userinfo_response.json()
        st.session_state.auth0_user['userinfo'] = userinfo
        st.query_params.clear()
    except Exception as e:
        st.error(f"An error occurred during callback: {str(e)}")
        st.write("Debug info:")
        st.write(f"Params: {params}")
        st.write(f"State: {st.session_state.auth0_state}")

def logout():
    st.session_state.auth0_user = None
    st.session_state.auth0_state = None

def get_user_info():
    return st.session_state.auth0_user

import streamlit as st
import os
from authlib.integrations.requests_client import OAuth2Session
from starlette.config import Config
import requests
from urllib.parse import urlencode
import hashlib

from custom_pages.home import home_page
from custom_pages.about import about_page
from custom_pages.snap import snap_page
from custom_pages.recipe import recipe_page
from custom_pages.meal import meal_page


def is_authenticated():
    return st.session_state.auth0_user is not None

def get_gravatar_url(email, size=80):
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"

def main():
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #2E3192 0%, #1BFFFF 100%);
            color: gold;
        }
        .sidebar img {
            border-radius: 50%;
            border: 2px solid gold;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }
        .sidebar .st-bw {
            background-color: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .sidebar .st-eb {
            font-weight: bold;
        }
        .sidebar .st-bq {
            padding: 5px 10px;
            border-radius: 20px;
            background-color: rgba(255,255,255,0.2);
            margin-bottom: 5px;
            transition: background-color 0.3s ease;
        }
        .sidebar .st-bq:hover {
            background-color: rgba(255,255,255,0.3);
        }
        .user-info {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .user-info img {
            margin-right: 10px;
        }
        .logout-button {
            background-color: rgba(255,255,255,0.2);
            color: gold;
            border: none;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .logout-button:hover {
            background-color: rgba(255,255,255,0.3);
        }
        </style>
    """, unsafe_allow_html=True)

    params = st.query_params
    if 'code' in params and 'state' in params:
        callback()
        st.rerun()

    with st.sidebar:
        st.title("🍽️ SnapChef")
        st.markdown("---")

        if is_authenticated():
            user_info = get_user_info()['userinfo']
            gravatar_url = get_gravatar_url(user_info['email'])

            st.markdown(
                f"""
                <div class="user-info">
                    <img src="{gravatar_url}" width="50">
                    <div>
                        <strong>{user_info['name']}</strong><br>
                        <small>{user_info['email']}</small>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("You are not logged in.")
            if st.button("🔐 Login", key="login_button"):
                login()

        st.markdown("---")
        st.subheader("📍 Navigation")

        pages = [
            {"name": "🏠 Home", "protected": False},
            {"name": "ℹ️ About", "protected": False},
            {"name": "📷 Snap", "protected": True},
            {"name": "📚 Recipe Assistant", "protected": True},
            {"name": "🍳 Meal Ideas", "protected": True}
        ]

        selected_page = st.radio(
            "",
            [p["name"] for p in pages],
            format_func=lambda x: f"{x} 🔒" if [p for p in pages if p['name'] == x][0]["protected"] and not is_authenticated() else x
        )

        if is_authenticated():
            st.markdown("---")
            st.subheader("📊 Your Stats")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Recipes Created", "15")
            with col2:
                st.metric("Favorites", "7")

            st.markdown("---")
            st.subheader("🔍 Quick Search")
            search_query = st.text_input("Search recipes...", key="search_bar")
            if search_query:
                st.info(f"Searching for: {search_query}")

            st.markdown("---")
            theme_options = ["Light", "Dark"]
            current_theme = st.session_state.get('theme', "Dark")
            new_theme = st.select_slider(
                "🎨 Color Theme",
                options=theme_options,
                value=current_theme
            )
            if new_theme != current_theme:
                st.session_state.theme = new_theme
                st.info(f"Theme preference set to: {new_theme}. Please restart the app for changes to take effect.")
                if st.button("Restart App"):
                    st.rerun()

            st.markdown("---")
            if st.button("🚪 Logout", key="logout", help="Click to log out"):
                logout()
                st.rerun()

    selected_page_info = next(p for p in pages if p["name"] == selected_page)
    if not selected_page_info["protected"] or is_authenticated():
        if "Home" in selected_page:
            home_page()
        elif "About" in selected_page:
            about_page()
        elif "Snap" in selected_page:
            snap_page()
        elif "Recipe Assistant" in selected_page:
            recipe_page()
        elif "Meal Ideas" in selected_page:
            meal_page()
    else:
        st.warning("You need to log in to access this page.")
        st.info("Please log in using the sidebar.")

if __name__ == "__main__":
    main()
