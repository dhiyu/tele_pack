#coding:utf-8
'''用户日志保存：
将用户ID和用户输入的需求套餐保存到log.txt文件中
输入：字符串（包括用户ID和4个数据）
输出："save_success"
错误：file_error'''


import time
import file_process


def receive_user_log(log):
    t = time.localtime(time.time())
    str = log + ' ' + time.asctime(t) + '\n'
    log = log.split()
    logs = file_process.read_item("user_log.txt", "r")
    for item in logs:
        item = item.split()
        if item[0:5] == log[0:5]:
            return "记录已存在"
    list = []
    list.append(str)
    return file_process.write_to_file("user_log.txt", list, "a+")



#print(receive_user_log("shiyu969696999696969696969"))