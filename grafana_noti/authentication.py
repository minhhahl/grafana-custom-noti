import os
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

AUTH_USERNAME = os.getenv('AUTH_USERNAME', 'admin')
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD', 'admin')

USER_DATA = {
    AUTH_USERNAME: AUTH_PASSWORD
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False

    return USER_DATA.get(username) == password
