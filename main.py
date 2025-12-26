from src.user import User, OutSchoolUser
from src.host.host import cc98_initialize, is_in_school_net, vpn_initialize

if __name__ == '__main__':
    user_name, passwd = cc98_initialize()
    if is_in_school_net():
        user = User(user_name, passwd)
        user.main_logic()
    else:
        studentid, password = vpn_initialize()
        out_school_user = OutSchoolUser(cc98_username = user_name, cc98_password=passwd, vpn_studentid=studentid, vpn_password=password)
        out_school_user.main_logic() 
