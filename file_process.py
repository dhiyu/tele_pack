#coding:utf-8
'''优惠套餐文件处理接口：
读取所有套餐:
    read_item()
输入值:空
输出值:所有项目列表
查找返回值：
    search_item_by_id(search_id)
输入值:ID
输出值:列表形式(只有一个元素)(字符串型)
未找到项目:"not_found_item"
增加一条:add_to_list(char_list content)
输入类型：字符串(所有信息)
输出：添加成功："save_success"
     添加失败："file_error"
修改一条 change_item(package_code,new_package)
输入类型：套餐编号，新套餐(字符串)
输出：保存成功:"save_success"
     文件错误:"file_error"
     未找到套餐:"not_found_item"
删除一条 detele_item(char_list content)
输入类型：字符串(套餐ID)
输出：删除成功:"delete_success"
     写入文件失败："file error"
     找不到项目:"item_not_found"
'''
#打开文件模块，如果不存在直接新建文件


def add_to_list(content):
    package_id = content.split()[0]
    if is_exist(package_id) == 1:
        return "套餐ID已存在，请重新制定"
    try:
        with open('data.txt', 'a+') as f:
            f.write(content+'\n')
    except FileNotFoundError:
        return "file_error"
    else:
        return "save_success"


def read_item(route, way):
    try:
        with open(route, way) as f:
            data = f.readlines()
    except FileNotFoundError:
            return "file_error"
    else:
            return data


def search_item_by_id(search_id):
    p = []
    items = read_item('data.txt', 'r+')
    for item in items:
        package_id =item.split()[0]
        if package_id == search_id:
            p.append(item)
    if len(p) == 0:
        return "not_found_item"
    return p


def detele_item(id):
    items = read_item('data.txt', 'r+')
    for item in items:
        package_id = item.split()[0]
        if package_id == id:
            items.remove(item)
            if write_to_file('data.txt', items, 'w+') == "save_success":
                return "delete_success"
            else:
                return "file error"
    return "item_not_found"


#  改套餐
def change_item(package_code,new_package):
    all_data = read_item('data.txt', 'r+')
    for item in all_data:
        if package_code == item.split()[0]:
            all_data[all_data.index(item)] = new_package+'\n'
            if write_to_file('data.txt', all_data, 'w+') =="save_success":
                return "save_success"
            else:
                return "file_error"
    return "not_found_item"


#写文件
def write_to_file(routes, items, way):
    try:
        with open(routes, way) as f:
            f.writelines(items)
    except FileNotFoundError:
        return "file_error"
    else:
        return "save_success"


#检测套餐是否存在
def is_exist(package_id):
    items = read_item('data.txt', 'r')
    for item in items:
        item = item.split()
        if package_id == item[0]:
            return 1
    return 0


#测试函数
#add_to_list("shiyu123shenguoqiang123baokaixuan123")
#print(change_item("content"))
#print(search_item_by_id("乐享4G-39元"))
#detele_item("shiyu")
#print(change_item("B01030556","shiyu 6666 shiyu 6666 shiyu 6666"))
#print(read_item("user_choice.txt",'r'))