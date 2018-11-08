#coding:utf-8

import file_process


def read_user_log():
    return file_process.read_item("user_log.txt",'r')


#print(read_user_log())