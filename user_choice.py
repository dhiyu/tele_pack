#coding:utf-8
'''用户套餐选择保存：
输入：字符串（用户ID+空格+套餐id）
返回值"save_success"
错误值"file_error"'''


import time
import file_process
import admin_user_choice


def save_user_choice(user_choice):
    t = time.localtime(time.time())
    str = user_choice + ' ' + time.asctime(t) + '\n'
    user_choice = user_choice.split()
    user = user_choice[0]
    choices = file_process.read_item("user_choice.txt", "r")
    for choice in choices:
        choice = choice.split()
        if choice[0] == user:
            return admin_user_choice.change_package(user, user_choice[1])
    list = []
    list.append(str)
    return file_process.write_to_file("user_choice.txt", list, "a+")



#print(save_user_choice("shenguoqiang 天翼4g"))