'''推荐算法模块：
核心函数：recommend_package(user_want_package)
传入值：字符串：样例（“100 100 50G 100M”）
包括费用 分钟数 流量 宽带
传出值：包含套餐编号的列表，用于索引相应的套餐值'''


from file_process import *


def type_convert(item):
    package = item.split()
    print(package)
    cost = package[1]
    talk_time = package[2]
    data_4g = package[3]
    WBBW = package[4]
    if WBBW[-1] == 'm' or WBBW[-1] =='M':
        WBBW = float(WBBW[:-1])
    else:
        return "WBBW_ERROR"
    if data_4g[-1] == 'm' or data_4g[-1] == 'M':
        data_4g = float(data_4g[:-1]) / 1024
    elif data_4g[-1] == 'g' or data_4g[-1] == 'G':
        data_4g = float(data_4g[:-1])
    else:
        return 'data_4g_error'
    cost = float(cost)
    talk_time = float(talk_time)
    WBBW = float(WBBW)
    p = [cost, talk_time/50, data_4g*2, WBBW/50]
    return p


def convert_to_vector():
    item_dict = {}
    items = read_item('data.txt', 'r')
    if items == "file_error":
        return "file_error"
    for item in items:
        item_dict.update({item.split()[0]: type_convert(item)})
    return item_dict


def sort_dict(dict):
    dict = sorted(dict.items(), key = lambda d: d[1])
    recommend_dict = [list(i) for i in dict]
    return recommend_dict


def recommend_package(user_want_package):
    user_want_package = "want " + user_want_package
    user_want = type_convert(user_want_package)
    items_dict = convert_to_vector()
    if user_want != 'data_4g_error' and items_dict != "file_error" and user_want != "WBBW_ERROR":
        for item_key in items_dict.keys():
            item = items_dict.get(item_key)
            add = 0
            for i in range(0, 4):
                if user_want[i] != 0:
                    add += pow((user_want[i]-float(item[i])), 2)
            add = pow(add, 1/2)
            items_dict[item_key] = add
        sorted_dict = sort_dict(items_dict)
        standard_value = sorted_dict[0][1]
        if standard_value != 0:
            for i in sorted_dict:
                i[1] = standard_value / i[1]
        return sorted_dict
    else:
        return "input_or_file_error"


#print(recommend_package("100 0 0G 1000M"))