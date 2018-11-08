#coding:utf-8
'''统计套餐模块：
返回类型：['shiyu969696999696969696969Wed Oct 24 10:41:27 2018\n',
'shiyu969696999696969696969 Wed Oct 24 10:42:54 2018\n']此种形式的列表
错误类型：file_error'''


import file_process


def count_users_in_package():
    users = file_process.read_item("user_choice.txt", 'r')
    if users == "file_error":
        return users
    packages = file_process.read_item("data.txt", 'r')
    if packages == "file_error":
        return packages
    i = 0
    for package in packages:
        count = 0
        package = package.split()
        for user in users:
            user = user.split()
            if user[1] == package[0]:
                count += 1
        packages[i] = [package[0], count]
        i += 1
    return packages


#print(count_users_in_package())