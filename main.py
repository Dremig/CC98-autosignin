from src.user import User
from src.host.host import initialize
import os

if __name__ == '__main__':
    user_name, passwd = initialize()
    user = User(user_name, passwd)
    user.main_logic()
