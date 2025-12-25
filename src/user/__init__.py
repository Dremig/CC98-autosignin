import requests
from ..host.host import renew

class User:
    TOKEN_URL = "https://openid.cc98.org/connect/token"
    LOGIN_URL = "https://api.cc98.org/me/signin"
    CLIENT_ID = "9a1fd200-8687-44b1-4c20-08d50a96e5cd"
    CLIENT_SECRET = "8b53f727-08e2-4509-8857-e34bf92b27f2"
    GRANT_TYPE = "password"

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def get_token(self):
        data = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET, 
            "grant_type": self.GRANT_TYPE,
            "username": self.username,
            "password": self.password
        }

        response = requests.post(self.TOKEN_URL, data=data)
        if not response.json().get("access_token"):
            print("It seems that what your account is invalid, please enter them again")
            user_name, password = renew()
            self.__init__(user_name, password)
            response = requests.post(self.TOKEN_URL, data=data)
        return response.json().get("access_token")
    
    def login(self):
        header = {
            "Authorization": "Bearer " + self.get_token()
        }

        response = requests.get(self.LOGIN_URL, headers=header)
        return response.json()
    
    def parse_info(self):
        pass