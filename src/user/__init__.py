import requests
from ..host.host import renew
import json
import datetime

class User:
    TOKEN_URL = "https://openid.cc98.org/connect/token"
    LOGIN_URL = "https://api.cc98.org/me/signin"
    QUERY_URL = "https://api.cc98.org/me/signin-in-month?year=114514&month=1919810"
    CLIENT_ID = "9a1fd200-8687-44b1-4c20-08d50a96e5cd"
    UNREAD_COUNT = "https://api.cc98.org/me/unread-count"
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
        result = response.json()
        # print()
        login_success = self.get_day_signin_ornot()
        if login_success:
            print("Login success!")
            # print("You have sign in for %d days")
            print("You received %d reward", result["lastReward"])
        else:
            print("Login failed. Please check your account.")


        
    
    def get_day_signin_ornot(self):
        header = {
            "Authorization": "Bearer " + self.get_token()
        }
        query_url = self.QUERY_URL.replace("114514", str(datetime.datetime.now().year)).replace("1919810", str(datetime.datetime.now().month))
        # print(query_url)

        response = requests.get(query_url, headers=header)
        if len(response.json()) > 0:
            today = response.json()[-1]
            if today["day"] != datetime.datetime.now().day:
                # not signed in
                return False
            else:
                return True
        return False
    
    def main_logic(self):
        if not self.get_day_signin_ornot():
            # not signed in
            self.login()
        else:
            print("You have already signed in today")
    

