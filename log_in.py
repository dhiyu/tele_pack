#coding:utf-8
'''登录认证子文件使用说明'''
'''主函数 login(id,password)'''
'''传入值类型：字符串'''
'''返回值类型：字符串'''
'''管理员认证成功返回值"login_success_with_admin"'''
'''一般用户认证成功返回值"login_success_with_user"'''
'''其他错误："id_not_found","password_error"'''
import zlib


def read_user():
    try:
        with open('login.txt', 'r+') as f:
            user_data = f.readlines()
    except FileNotFoundError:
            return "file_error"
    else:
            return user_data


def login(id,password):
    users = read_user()
    for user in users:
        if user.split()[0] == id:
            if user.split()[1] == encode(password):
                if user.split()[2] == "admin":
                    return "login_success_with_admin"
                else:
                    return "login_success_with_user"
            else:
                return "password_error"
    return "id_not_found"


#def decode(password):


def encode(password):
    password = bytes(password, encoding="utf-8")
    return str(zlib.crc32(password))


#print(login("shiyu","123456"))