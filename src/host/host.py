import os
def initialize():
    if not os.path.exists('.env'):
        if os.path.exists('env.example'):
            print("I assumed you use this project for the first time. I will create a .env file for you.")
        user_name = input("Enter your CC98 username: ")
        passwd = input("Enter your CC98 password: ")
        with open('.env', 'w') as f:
            f.write(f'CC98_USERNAME={user_name}\nCC98_PASSWORD={passwd}')
    else:
        with open('.env', 'r') as f:
            lines = f.readlines()
            user_name = lines[0].split('=')[1].strip()
            passwd = lines[1].split('=')[1].strip()

    return user_name, passwd

def renew():
    user_name = input("Enter your CC98 username: ")
    passwd = input("Enter your CC98 password: ")
    with open('.env', 'w') as f:
        f.write(f'CC98_USERNAME={user_name}\nCC98_PASSWORD={passwd}')
    return user_name, passwd
        