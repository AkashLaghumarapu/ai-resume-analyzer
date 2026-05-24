import streamlit_authenticator as stauth

credentials = {
    "usernames": {
        "admin": {
            "name": "Admin User",
            "password": stauth.Hasher.hash("password123")
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "resume_analyzer",
    "abcdef",
    cookie_expiry_days=1
)

def load_authenticator():
    return authenticator