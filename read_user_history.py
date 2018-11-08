#coding:utf-8
'''读取用户近六个月消费行为的模块
主函数：read_user_history(user_id)
传入值：字符串型用户ID
传出值：二维列表 类似[['29', '71', '97M', '12M'], ['39', '84', '88M', '12M'], ['49', '101', '163M', '20M'], ['59', '114', '169M', '20M'],
['59', '126', '201M', '20M'], ['79', '251', '307', '50M']]
每个行元素代表一个月的记录
错误类型：未找到用户："not_found_user"'''


import file_process


def read_user_history(user_id):
    user_history = file_process.read_item("user_history.txt", "r")
    for user_item in user_history:
        user_item = user_item.split()
        if user_item[0] == user_id:
            p = []
            for i in range(0, 6):
                cost = user_item[5 * i + 2]
                talk_time = user_item[5 * i + 3]
                data_4g = user_item[5 * i + 4]
                WBBW = user_item[5 * i + 5]
                p.append([cost, talk_time, data_4g, WBBW])
            return p
    return "not_found_user"


#print(read_user_history("jobs.bao"))