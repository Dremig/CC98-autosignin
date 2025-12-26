import os
import json
import requests
import shutil


def cc98_initialize():
    '''
    init username and password for vpn in config.json
    '''
    if not os.path.exists('config.json'):
        if os.path.exists('config.json.example'):
            print("I assumed you use this project for the first time. I will create a config file for you.")
            shutil.copy('config.json.example', 'config.json')
        user_name = input("Enter your CC98 username: ")
        passwd = input("Enter your CC98 password: ")
        with open('config.json', 'r') as f:
            content = f.read()
        config = json.loads(content)
        config['CC98_USERNAME'] = user_name
        config['CC98_PASSWORD'] = passwd
        with open('config.json', 'w') as f:
            f.write(json.dumps(config))
            
    else:
        with open('config.json', 'r') as f:
            content = f.read()
        config = json.loads(content)
        user_name = config['CC98_USERNAME']
        passwd = config['CC98_PASSWORD']

    return user_name, passwd

def cc98_renew():
    '''
    update username and password for cc98 in config.json
    '''
    user_name = input("Enter your CC98 username: ")
    passwd = input("Enter your CC98 password: ")
    with open('config.json', 'r') as f:
        content = f.read()
    config = json.loads(content)
    config['CC98_USERNAME'] = user_name
    config['CC98_PASSWORD'] = passwd
    with open('config.json', 'w') as f:
        f.write(json.dumps(config))
        
    return user_name, passwd


def vpn_initialize():
    '''
    init username and password for vpn in config.json
    '''
    if not os.path.exists('config.json'):
        cc98_renew()
    with open('config.json', 'r') as f:
        content = f.read()
    config = json.loads(content)
    if config['STUDENT_ID'] == "114514414141" and config['VPN_PASSWORD'] == "THIS_IS_A_SECRET":
        return vpn_renew()
    return config['STUDENT_ID'], config['VPN_PASSWORD']


def vpn_renew():
    '''
    init username and password for vpn in config.json
    '''
    student_id = input("Enter your VPN username: ")
    passwd = input("Enter your VPN password: ")
    with open('config.json', 'r') as f: 
        content = f.read()
    config = json.loads(content)
    config['STUDENT_ID'] = student_id
    config['VPN_PASSWORD'] = passwd
    with open('config.json', 'w') as f:
        f.write(json.dumps(config))

    return student_id, passwd


def is_in_school_net():
    '''
    check if the computer is in school net
    '''
    try: 
        re = requests.get('https://www.cc98.org', timeout=5)
    except requests.exceptions.RequestException:
        return False
    return re.status_code == 200