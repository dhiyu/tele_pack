#coding: utf-8
'''用户输入合法性判断
主要判断空格与空字符
'''
import re


def judge_str(str):
    pattern = re.compile(u'\s')
    if str.find(' ') != -1:
        return "输入中不能包含空格,请重新输入"
    elif re.search(pattern, str):
        #print(re.search(pattern, str))
        return "输入中含有空字符，请重新输入"
    else:
        return True


def judge_digtal(str):
    if  not str.isdigit():
        return "请输入大于0纯数字"
    else:
        try:
            if float(str) >= 0:
                return True
            else:
                return "请输入大于0纯数字"
        except:
            return "请输入大于0纯数字"



#print(judge_str('\n'))