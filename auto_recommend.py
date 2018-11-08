#coding:utf-8
'''自动推荐程序：
根据用户消费历史智能推荐
输入：用户ID
输出包含套餐编号的列表，用于索引相应的套餐值
错误值：数学错误"math_error"'''

import file_process
import recommend


def auto_recommend(user_id):
    user_history = file_process.read_item("user_history.txt", "r")
    #print(user_history)
    for item in user_history:
        item = item.split()
        cost = 0
        talk_time = 0
        data_4g = 0
        WBBW = 0
        #print(item)
        if item[0] == user_id:
            for i in range(0, 6):
                try:
                    cost += float(item[5*i+2]) / 6
                    talk_time += float(item[5*i+3]) / 6
                    data = float(item[5 * i + 4][:-1])
                    if item[5*i+4][-1] == 'M' or item[5*i+4][-1] == 'm':
                        data /= 1024
                    data_4g += data
                    WBBW += float(item[5*i+5][:-1]) / 6
                except TypeError:
                    return "math_error"
            history = str(cost) + ' ' + str(talk_time) + ' ' + str(data_4g) +'m ' + str(WBBW) + 'm'
    return recommend.recommend_package(history)


#print(auto_recommend("shiyu"))