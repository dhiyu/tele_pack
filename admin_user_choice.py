#coding:utf-8


'''管理用户优惠套餐模块
主函数change_package(user_id,new_package)改用户套餐
返回类型："save_success"
错误有："file_error" "not_found_item"
read_user_choice(user_id)读取单个用户
错误有："not_found_user"
read_users_choice()读取所有用户
'''


import time
import file_process


def change_package(user_id, new_package):
    all_data = file_process.read_item('user_choice.txt', 'r+')
    for item in all_data:
        if user_id == item.split()[0]:
            t = time.localtime(time.time())
            all_data[all_data.index(item)] = user_id + ' ' + new_package + ' ' + time.asctime(t) + '\n'
            if file_process.write_to_file('user_choice.txt', all_data, 'w+') == "save_success":
                return "save_success"
            else:
                return "file_error"
    return "not_found_item"


def read_user_choice(user_id):
    all_data = file_process.read_item('user_choice.txt', 'r')
    for item in all_data:
        if user_id == item.split()[0]:
            #print(item.split()[1])
            return file_process.search_item_by_id(item.split()[1])
    return "not_found_user"


def read_users_choice():
    return file_process.read_item('user_choice.txt', 'r+')


#print(change_package("shenguoqiang","超级VIP套餐"))
#print(read_user_choice("shenguoqiang"))