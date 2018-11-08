from tkinter import *
from log_in import *
from file_process import *
from tkinter import ttk
from recommend import *
from user_log import *
from user_choice import *
import copy
from auto_recommend import *
from admin_user_choice import *
from read_user_history import *
from count_users_in_packages import *
from admin_user_log import *
from judge_input import *





#初始化root列表
root_list = []






#root处理

#添加root
def add_root_to_rootlist(root):
    if root not in root_list:
        root_list.append(root)


#去除root
def destroy_root():
    for root in root_list:
        root.destroy()
        root_list.remove(root)



#管理员-用户数据

#管理员-用户数据-窗口
def admin_userdata_windows(root):
    global main_frame_admin_userdata1
    main_frame_admin_userdata1 = Frame(root)

    main_frame_admin_userdata1_l1 = Label(main_frame_admin_userdata1, text='选择各套餐的用户人数：', font=('微软雅黑', 11), height=2).grid(row=0, column=0, sticky=W)
    main_frame_admin_userdata1_l2 = Label(main_frame_admin_userdata1, text='用户意向：', font=('微软雅黑', 11), height=2).grid(row=0, column=2)
    main_frame_admin_userdata1_l3 = Label(main_frame_admin_userdata1, text='                                         ', font=('微软雅黑', 11), height=2).grid(row=0, column=1, rowspan=1)

    main_frame_admin_userdata1.grid(row=0, column=0, columnspan=3, sticky=W)

    global main_frame_admin_userdata2
    main_frame_admin_userdata2 = Frame(root)

    main_frame_admin_userdata2_sb1 = Scrollbar(main_frame_admin_userdata2)
    main_frame_admin_userdata2_sb1.pack(side=RIGHT, fill=Y)

    main_frame_admin_userdata2_lb1 = Listbox(main_frame_admin_userdata2, yscrollcommand=main_frame_admin_userdata2_sb1.set, font=('微软雅黑', 11), width=30, height=16)
    for item in count_users_in_package():
        main_frame_admin_userdata2_lb1.insert(END, str(item))
    main_frame_admin_userdata2_lb1.pack(side=LEFT, fill=BOTH)

    main_frame_admin_userdata2_sb1.config(command=main_frame_admin_userdata2_lb1.yview)

    main_frame_admin_userdata2.grid(row=1, column=0)

    global main_frame_admin_userdata3
    main_frame_admin_userdata3 = Frame(root)

    main_frame_admin_userdata3_l3 = Label(main_frame_admin_userdata3, text='          ', font=('微软雅黑', 11), height=2).grid(row=0, column=0)

    main_frame_admin_userdata3.grid(row=1, column=1)

    global main_frame_admin_userdata4
    main_frame_admin_userdata4 = Frame(root)


    main_frame_admin_userdata4_sb2 = Scrollbar(main_frame_admin_userdata4)
    main_frame_admin_userdata4_sb2.pack(side=RIGHT, fill=Y)
    main_frame_admin_userdata4_sb3 = Scrollbar(main_frame_admin_userdata4, orient=HORIZONTAL)
    main_frame_admin_userdata4_sb3.pack(side=BOTTOM, fill=X)

    main_frame_admin_userdata4_lb2 = Listbox(main_frame_admin_userdata4, yscrollcommand=main_frame_admin_userdata4_sb2.set, xscrollcommand=main_frame_admin_userdata4_sb3.set, font=('微软雅黑', 11), width=45, height=16)
    for item in read_user_log():
        main_frame_admin_userdata4_lb2.insert(END, str(item))
    main_frame_admin_userdata4_lb2.pack(side=LEFT, fill=BOTH)

    main_frame_admin_userdata4_sb2.config(command=main_frame_admin_userdata4_lb2.yview)
    main_frame_admin_userdata4_sb3.config(command=main_frame_admin_userdata4_lb2.xview)


    main_frame_admin_userdata4.grid(row=1, column=2)


#管理员-用户数据-根
def admin_userdata():
    destroy_root()
    global root_admin_userdata
    root_admin_userdata = Tk()
    add_root_to_rootlist(root_admin_userdata)
    root_admin_userdata.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_userdata.winfo_screenwidth() - 800) / 2, (root_admin_userdata.winfo_screenheight() - 400) / 2))
    root_admin_userdata.title('管理员-用户数据')

    admin_windows(root_admin_userdata)
    admin_userdata_windows(root_admin_userdata)



#管理员-用户信息

#管理员-用户信息-修改-列表

#管理员-用户信息-修改-列表-命令
def admin_userinfo_change_command1():
    global main_frame_admin_userinfo_change_list
    main_frame_admin_userinfo_change_list = Frame(root_admin_userinfo_list)

    main_frame_admin_userinfo_change_list_l1 = Label(main_frame_admin_userinfo_change_list, textvariable=admin_userinfo_change_v1, font=('微软雅黑', 10)).grid(row=0, column=0)

    print (user_name1)
    if read_user_choice(user_name1) == "not_found_user":
        admin_userinfo_change_v1.set('没有该用户')
    else:
        admin_userinfo_change_v1.set('当前用户现用套餐为：' + read_user_choice(user_name1)[0])

        package = read_item('data.txt', 'r')
        for item in package:
            if item == read_user_choice(user_name1)[0]:
                package.remove(item)

        global user_choice
        user_choice = tuple(package)



        main_frame_admin_userinfo_change_list_l3 = Label(main_frame_admin_userinfo_change_list, text='请选择要更改的套餐:    ', font=('微软雅黑', 11), height=2).grid(row=2, column=0)

        global main_frame_admin_userinfo_change_list_c1
        print (9527)
        print (user_choice)
        main_frame_admin_userinfo_change_list_c1 = ttk.Combobox(main_frame_admin_userinfo_change_list, width=30, state='readonly', font=('微软雅黑', 10))
        main_frame_admin_userinfo_change_list_c1['values'] = user_choice
        main_frame_admin_userinfo_change_list_c1.current(0)
        main_frame_admin_userinfo_change_list_c1.grid(row=3, column=0)


        main_frame_admin_userinfo_change_list_b2 = Button(main_frame_admin_userinfo_change_list, text='确定', command=admin_userinfo_change_command2, font=('微软雅黑', 11)).grid(row=4, column=0)

        main_frame_admin_userinfo_change_list_l4 = Label(main_frame_admin_userinfo_change_list, textvariable=admin_userinfo_change_v2).grid(row=5, column=0)

    main_frame_admin_userinfo_change_list.grid(row=2, column=1)



def admin_userinfo_change_command2():
    new_package = main_frame_admin_userinfo_change_list_c1.get().split()[0]
    print(new_package)
    if change_package(user_name1, new_package) == "not_found_item":
        admin_userinfo_change_v2.set('没有找到套餐')
    elif change_package(user_name1, new_package) == "file_error":
        admin_userinfo_change_v2.set('保存失败')
    else:
        admin_userinfo_change_v2.set('保存成功')

    main_frame_admin_userinfo_window_windows(root_admin_userinfo_list)

#管理员-用户信息-修改-列表-根
def admin_userinfo_list():
    global user_name1
    user_name1 = main_frame_admin_userinfo_change_e1.get()

    destroy_root()
    global root_admin_userinfo_list
    root_admin_userinfo_list = Tk()
    add_root_to_rootlist(root_admin_userinfo_list)
    root_admin_userinfo_list.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_userinfo_list.winfo_screenwidth() - 800) / 2, (root_admin_userinfo_list.winfo_screenheight() - 400) / 2))
    root_admin_userinfo_list.title('管理员-用户信息')

    global admin_userinfo_change_v1
    admin_userinfo_change_v1 = StringVar()
    global admin_userinfo_change_v2
    admin_userinfo_change_v2 = StringVar()

    admin_windows(root_admin_userinfo_list)
    main_frame_admin_userinfo_window_windows(root_admin_userinfo_list)
    admin_userinfo_change_windows(root_admin_userinfo_list)
    admin_userinfo_change_command1()



#管理员-用户信息-修改

#管理员-用户信息-修改-窗口
def admin_userinfo_change_windows(root):
    global main_frame_admin_userinfo_change
    main_frame_admin_userinfo_change = Frame(root)

    main_frame_admin_userinfo_change_l1 = Label(main_frame_admin_userinfo_change, text='请输入待修改用户名:     ', font=('微软雅黑', 11)).grid(row=0, column=0)
    main_frame_admin_userinfo_change_l2 = Label(main_frame_admin_userinfo_change, text='        ').grid(row=0, column=2, rowspan=6)

    global main_frame_admin_userinfo_change_e1
    main_frame_admin_userinfo_change_e1 = Entry(main_frame_admin_userinfo_change)
    main_frame_admin_userinfo_change_e1.grid(row=0, column=1)


    main_frame_admin_userinfo_change_b1 = Button(main_frame_admin_userinfo_change, text='确定', command=admin_userinfo_list, font=('微软雅黑', 11)).grid(row=0, column=3)


    main_frame_admin_userinfo_change.grid(row=1, column=1)



#管理员-用户信息-窗口
def main_frame_admin_userinfo_window_windows(root):
    global main_frame_admin_userinfo_window
    main_frame_admin_userinfo_window = Frame(root)

    main_frame_admin_userinfo_window_sb1 = Scrollbar(main_frame_admin_userinfo_window)
    main_frame_admin_userinfo_window_sb1.pack(side=RIGHT, fill=Y)
    main_frame_admin_userinfo_window_sb2 = Scrollbar(main_frame_admin_userinfo_window,  orient=HORIZONTAL)
    main_frame_admin_userinfo_window_sb2.pack(side=BOTTOM, fill=X)

    main_frame_admin_userinfo_window_lb1 = Listbox(main_frame_admin_userinfo_window, yscrollcommand=main_frame_admin_userinfo_window_sb1.set, xscrollcommand=main_frame_admin_userinfo_window_sb2.set, font=('微软雅黑', 11), width=40, height=17)
    for item in read_users_choice():
        main_frame_admin_userinfo_window_lb1.insert(END, str(item))
    main_frame_admin_userinfo_window_lb1.pack(side=LEFT, fill=BOTH)

    main_frame_admin_userinfo_window_sb1.config(command=main_frame_admin_userinfo_window_lb1.yview)
    main_frame_admin_userinfo_window_sb2.config(command=main_frame_admin_userinfo_window_lb1.xview)


    main_frame_admin_userinfo_window.grid(row=1, column=0, rowspan=2)


def main_frame_admin_userinfo_windows(root):
    global main_frame_admin_userinfo
    main_frame_admin_userinfo= Frame(root)

    main_frame_admin_userinfo_b1 = Button(main_frame_admin_userinfo, text='修改用户套餐', command=admin_userinfo_change_windows).grid(row=0, column=0)

    main_frame_admin_userinfo.grid(row=1, column=1)



#管理员-用户信息-根
def admin_userinfo():
    destroy_root()
    global root_admin_userinfo
    root_admin_userinfo = Tk()
    add_root_to_rootlist(root_admin_userinfo)
    root_admin_userinfo.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_userinfo.winfo_screenwidth() - 800) / 2, (root_admin_userinfo.winfo_screenheight() - 400) / 2))
    root_admin_userinfo.title('管理员-用户信息')

    admin_windows(root_admin_userinfo)
    main_frame_admin_userinfo_window_windows(root_admin_userinfo)
    admin_userinfo_change_windows(root_admin_userinfo)





#管理员-管理-新增


#管理员-管理-新增-命令
def admin_command_add_command():
    number = main_frame_admin_management_command_add_e1.get()
    cost = main_frame_admin_management_command_add_e2.get()
    communication_length = main_frame_admin_management_command_add_e3.get()
    data = main_frame_admin_management_command_add_e4.get()
    internet = main_frame_admin_management_command_add_e5.get()

    data_SI =  main_frame_admin_management_command_add_c1.get()
    internet_SI =  main_frame_admin_management_command_add_c2.get()


    if judge_str(number) == "输入中不能包含空格,请重新输入":
        admin_management_add_v.set("输入中不能包含空格,请重新输入")
    elif judge_str(number) == "输入中含有空字符，请重新输入":
        admin_management_add_v.set("输入中含有空字符，请重新输入")
    elif number == '':
        admin_management_add_v.set("各输入项不能为空")
    elif judge_digtal(str(cost)) == "请输入大于0纯数字" or judge_digtal(str(communication_length)) == "请输入大于0纯数字" or judge_digtal(str(data)) == "请输入大于0纯数字" or judge_digtal(str(internet)) == "请输入大于0纯数字":
        admin_management_add_v.set("除套餐名称外请输入大于等于0纯数字")
    else:
        data = str(data) + str(data_SI)
        internet = str(internet) + str(internet_SI)

        insert_data = number + ' ' + cost + ' ' + communication_length + ' ' + data + ' ' + internet

        if add_to_list(insert_data) == "save_success":
            admin_management_add_v.set('添加成功')
        else:
            admin_management_add_v.set('添加失败')

    main_frame_admin_management_window_windows(root_admin_management_add)

#管理员-管理-新增-窗口
def main_frame_admin_management_command_add_windows(root):
    global main_frame_admin_management_command_add
    main_frame_admin_management_command_add = Frame(root)

    main_frame_admin_management_command_add_l1 = Label(main_frame_admin_management_command_add, text='套餐编号', font=('微软雅黑', 11), height=2).grid(row=0, column=0)
    main_frame_admin_management_command_add_l2 = Label(main_frame_admin_management_command_add, text='月资费', font=('微软雅黑', 11), height=2).grid(row=1, column=0)
    main_frame_admin_management_command_add_l3 = Label(main_frame_admin_management_command_add, text='通话时长', font=('微软雅黑', 11), height=2).grid(row=2, column=0)
    main_frame_admin_management_command_add_l4 = Label(main_frame_admin_management_command_add, text='4G流量', font=('微软雅黑', 11), height=2).grid(row=3, column=0)
    main_frame_admin_management_command_add_l5 = Label(main_frame_admin_management_command_add, text='宽带带宽', font=('微软雅黑', 11), height=2).grid(row=4, column=0)
    main_frame_admin_management_command_add_l6 = Label(main_frame_admin_management_command_add, text='        ').grid(row=0, column=3, rowspan=6)

    global main_frame_admin_management_command_add_e1
    main_frame_admin_management_command_add_e1 = Entry(main_frame_admin_management_command_add)
    main_frame_admin_management_command_add_e1.grid(row=0, column=1)
    global main_frame_admin_management_command_add_e2
    main_frame_admin_management_command_add_e2 = Entry(main_frame_admin_management_command_add)
    main_frame_admin_management_command_add_e2.grid(row=1, column=1)
    global main_frame_admin_management_command_add_e3
    main_frame_admin_management_command_add_e3 = Entry(main_frame_admin_management_command_add)
    main_frame_admin_management_command_add_e3.grid(row=2, column=1)
    global main_frame_admin_management_command_add_e4
    main_frame_admin_management_command_add_e4 = Entry(main_frame_admin_management_command_add)
    main_frame_admin_management_command_add_e4.grid(row=3, column=1)
    global main_frame_admin_management_command_add_e5
    main_frame_admin_management_command_add_e5 = Entry(main_frame_admin_management_command_add)
    main_frame_admin_management_command_add_e5.grid(row=4, column=1)

    global main_frame_admin_management_command_add_c1
    main_frame_admin_management_command_add_c1 = ttk.Combobox(main_frame_admin_management_command_add, width=2, state='readonly')
    main_frame_admin_management_command_add_c1['values'] = ('M', 'G')
    main_frame_admin_management_command_add_c1.current(0)
    main_frame_admin_management_command_add_c1.grid(row=3, column=2)
    global main_frame_admin_management_command_add_c2
    main_frame_admin_management_command_add_c2 = ttk.Combobox(main_frame_admin_management_command_add, width=2, state='readonly')
    main_frame_admin_management_command_add_c2['values'] = ('M')
    main_frame_admin_management_command_add_c2.current(0)
    main_frame_admin_management_command_add_c2.grid(row=4, column=2)

    main_frame_admin_management_command_add_b1 = Button(main_frame_admin_management_command_add, text='保存', command=admin_command_add_command, font=('微软雅黑', 11)).grid(row=0, column=4, rowspan=5)

    main_frame_admin_management_command_add_l3 = Label(main_frame_admin_management_command_add, textvariable=admin_management_add_v).grid(row=5, column=0, columnspan=5)

    main_frame_admin_management_command_add.grid(row=1, column=1)

#管理员-管理-新增-根
def admin_management_add():
    destroy_root()
    global root_admin_management_add
    root_admin_management_add = Tk()
    add_root_to_rootlist(root_admin_management_add)
    root_admin_management_add.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_management_add.winfo_screenwidth() - 800) / 2, (root_admin_management_add.winfo_screenheight() - 400) / 2))
    root_admin_management_add.title('管理员-管理-新增')

    global admin_management_add_v
    admin_management_add_v = StringVar()

    admin_windows(root_admin_management_add)
    main_frame_admin_management_window_windows(root_admin_management_add)
    main_frame_admin_management_command_add_windows(root_admin_management_add)




#管理员-管理-删除

#管理员-管理-删除-命令
def admin_command_delete_command():
    ID = main_frame_admin_management_command_delete_e1.get()

    if detele_item(str(ID)) == "item_not_found":
        admin_management_delete_v.set('没有找到对应ID的套餐')
    elif detele_item(str(ID)) == "file error":
        admin_management_delete_v.set('写入错误')
    else:
        admin_management_delete_v.set('删除成功')

        main_frame_admin_management_window_windows(root_admin_management_delete)


#管理员-管理-删除—窗口
def main_frame_admin_management_command_delete_windows(root):
    global main_frame_admin_management_command_delete
    main_frame_admin_management_command_delete = Frame(root)

    main_frame_admin_management_command_delete_l1 = Label(main_frame_admin_management_command_delete, text='请输入待删除套餐ID:     ', font=('微软雅黑', 11)).grid(row=0, column=0)
    main_frame_admin_management_command_delete_l2 = Label(main_frame_admin_management_command_delete, text='        ').grid(row=0, column=2)

    global main_frame_admin_management_command_delete_e1
    main_frame_admin_management_command_delete_e1 = Entry(main_frame_admin_management_command_delete)
    main_frame_admin_management_command_delete_e1.grid(row=0, column=1)

    main_frame_admin_management_command_delete_b1 = Button(main_frame_admin_management_command_delete, text='确定', font=('微软雅黑', 11), command=admin_command_delete_command).grid(row=0, column=3)

    main_frame_admin_management_command_delete_l2 = Label(main_frame_admin_management_command_delete, textvariable=admin_management_delete_v, font=('微软雅黑', 10)).grid(row=2, column=0, columnspan=4)

    main_frame_admin_management_command_delete.grid(row=1, column=1)

#管理员-管理-删除-根
def admin_management_delete():
    destroy_root()
    global root_admin_management_delete
    root_admin_management_delete = Tk()
    add_root_to_rootlist(root_admin_management_delete)
    root_admin_management_delete.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_management_delete.winfo_screenwidth() - 800) / 2, (root_admin_management_delete.winfo_screenheight() - 400) / 2))
    root_admin_management_delete.title('管理员-管理-删除')

    global admin_management_delete_v
    admin_management_delete_v = StringVar()

    admin_windows(root_admin_management_delete)
    main_frame_admin_management_window_windows(root_admin_management_delete)
    main_frame_admin_management_command_delete_windows(root_admin_management_delete)




#管理员-管理-修改-列表

#管理员-管理-修改-列表-命令
def admin_command_change_command1():
    print (23)

    if search_item_by_id(admin_management_change_ID) == "not_found_item":
        print(404)
        global main_frame_admin_management_command_change1
        main_frame_admin_management_command_change1 = Frame(root_admin_command_change_list)

        main_frame_admin_management_command_change1_l1 = Label(main_frame_admin_management_command_change1, textvariable=admin_management_change_v1, font=('微软雅黑', 10), height=2).pack()
        admin_management_change_v1.set('套餐不存在')


        main_frame_admin_management_command_change1.grid(row=2, column=1)


    else:
        print(502)
        global main_frame_admin_management_command_change2
        main_frame_admin_management_command_change2 = Frame(root_admin_command_change_list)

        main_frame_admin_management_command_change2_l7 = Label(main_frame_admin_management_command_change2, textvariable=admin_management_change_v1, font=('微软雅黑', 10), height=2).grid(row=1, column=0, columnspan=4)
        admin_management_change_v1.set('套餐存在，输入框内为该套餐原先内容')
        main_frame_admin_management_command_change2_l2 = Label(main_frame_admin_management_command_change2, text='        ').grid(row=0, column=2, rowspan=7)
        info = search_item_by_id(admin_management_change_ID)
        info_list = info[0].split()

        main_frame_admin_management_command_change2_l2 = Label(main_frame_admin_management_command_change2, text='月资费',font=('微软雅黑', 11)).grid(row=2, column=0)
        main_frame_admin_management_command_change2_l3 = Label(main_frame_admin_management_command_change2, text='通话时长',font=('微软雅黑', 11)).grid(row=3, column=0)
        main_frame_admin_management_command_change2_l4 = Label(main_frame_admin_management_command_change2, text='4G流量',font=('微软雅黑', 11)).grid(row=4, column=0)
        main_frame_admin_management_command_change2_l5 = Label(main_frame_admin_management_command_change2, text='宽带带宽',font=('微软雅黑', 11)).grid(row=5, column=0)

        global main_frame_admin_management_command_change2_e2
        main_frame_admin_management_command_change2_e2 = Entry(main_frame_admin_management_command_change2)
        main_frame_admin_management_command_change2_e2.insert(END, info_list[1])
        main_frame_admin_management_command_change2_e2.grid(row=2, column=1)
        global main_frame_admin_management_command_change2_e3
        main_frame_admin_management_command_change2_e3 = Entry(main_frame_admin_management_command_change2)
        main_frame_admin_management_command_change2_e3.insert(END, info_list[2])
        main_frame_admin_management_command_change2_e3.grid(row=3, column=1)
        global main_frame_admin_management_command_change2_e4
        main_frame_admin_management_command_change2_e4 = Entry(main_frame_admin_management_command_change2)
        main_frame_admin_management_command_change2_e4.insert(END, info_list[3][:-1])
        main_frame_admin_management_command_change2_e4.grid(row=4, column=1)
        global main_frame_admin_management_command_change2_e5
        main_frame_admin_management_command_change2_e5 = Entry(main_frame_admin_management_command_change2)
        main_frame_admin_management_command_change2_e5.insert(END, info_list[4][:-1])
        main_frame_admin_management_command_change2_e5.grid(row=5, column=1)

        global main_frame_admin_management_command_change2_c1
        main_frame_admin_management_command_change2_c1 = ttk.Combobox(main_frame_admin_management_command_change2, width=2, state='readonly')
        main_frame_admin_management_command_change2_c1['values'] = ('M', 'G')
        main_frame_admin_management_command_change2_c1.current(0)
        main_frame_admin_management_command_change2_c1.grid(row=4, column=2)
        global main_frame_admin_management_command_change2_c2
        main_frame_admin_management_command_change2_c2 = ttk.Combobox(main_frame_admin_management_command_change2, width=2, state='readonly')
        main_frame_admin_management_command_change2_c2['values'] = ('M')
        main_frame_admin_management_command_change2_c2.current(0)
        main_frame_admin_management_command_change2_c2.grid(row=5, column=2)

        main_frame_admin_management_command_change2_b2 = Button(main_frame_admin_management_command_change2, text='确定', command=admin_command_change_command2, font=('微软雅黑', 11)).grid(row=2, column=3, rowspan=4)

        main_frame_admin_management_command_change2_l6 = Label(main_frame_admin_management_command_change2, textvariable=admin_management_change_v2, font=('微软雅黑', 10)).grid(row=6, column=0, columnspan=4)

        main_frame_admin_management_command_change2.grid(row=2, column=1)


def admin_command_change_command2():
    ID = admin_management_change_ID
    cost = main_frame_admin_management_command_change2_e2.get()
    communication_length = main_frame_admin_management_command_change2_e3.get()
    data = main_frame_admin_management_command_change2_e4.get()
    internet = main_frame_admin_management_command_change2_e5.get()

    data_SI = main_frame_admin_management_command_change2_c1.get()
    internet_SI = main_frame_admin_management_command_change2_c2.get()


    if judge_digtal(str(cost)) == "请输入大于0纯数字" or judge_digtal(str(communication_length)) == "请输入大于0纯数字" or judge_digtal(str(data)) == "请输入大于0纯数字" or judge_digtal(str(internet)) == "请输入大于0纯数字":
        admin_management_change_v2.set("请输入大于等于0纯数字")

    else:
        data = str(data) + str(data_SI)
        internet = str(internet) + str(internet_SI)

        change_data = ID + ' ' + cost + ' ' + communication_length + ' ' + data + ' ' + internet

        if change_item(admin_management_change_ID, change_data) == "file_error":
            admin_management_change_v2.set('修改错误')
        elif change_item(admin_management_change_ID, change_data) == "save_success":
            admin_management_change_v2.set('修改成功')

            main_frame_admin_management_window_windows(root_admin_command_change_list)


#管理员-管理-修改-列表-根
def admin_command_change_list():
    global admin_management_change_ID
    admin_management_change_ID = main_frame_admin_management_command_change_e1.get()
    print (admin_management_change_ID)

    destroy_root()
    global root_admin_command_change_list
    root_admin_command_change_list = Tk()
    add_root_to_rootlist(root_admin_command_change_list)
    root_admin_command_change_list.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_command_change_list.winfo_screenwidth() - 800) / 2, (root_admin_command_change_list.winfo_screenheight() - 400) / 2))
    root_admin_command_change_list.title('管理员-管理-修改')

    global admin_management_change_v1
    admin_management_change_v1 = StringVar()

    global admin_management_change_v2
    admin_management_change_v2 = StringVar()

    admin_windows(root_admin_command_change_list)
    main_frame_admin_management_window_windows(root_admin_command_change_list)
    main_frame_admin_management_command_change_windows(root_admin_command_change_list)
    admin_command_change_command1()



#管理员-管理-修改

#管理员-管理-修改-窗口
def main_frame_admin_management_command_change_windows(root):
    global main_frame_admin_management_command_change
    main_frame_admin_management_command_change = Frame(root)

    main_frame_admin_management_command_change_l1 = Label(main_frame_admin_management_command_change, text='请输入待修改套餐ID: ', font=('微软雅黑', 11)).grid(row=0, column=0)
    main_frame_admin_management_command_change_l2 = Label(main_frame_admin_management_command_change, text='        ').grid(row=0, column=3,rowspan=7)

    global main_frame_admin_management_command_change_e1
    main_frame_admin_management_command_change_e1 = Entry(main_frame_admin_management_command_change)
    main_frame_admin_management_command_change_e1.grid(row=0, column=1)

    main_frame_admin_management_command_change_b1 = Button(main_frame_admin_management_command_change, text='确定', command=admin_command_change_list, font=('微软雅黑', 11)).grid(row=0, column=4)

    main_frame_admin_management_command_change.grid(row=1, column=1)


#管理员-管理-修改-根
def admin_management_change():
    destroy_root()
    global root_admin_management_change
    root_admin_management_change = Tk()
    add_root_to_rootlist(root_admin_management_change)
    root_admin_management_change.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_management_change.winfo_screenwidth() - 800) / 2, (root_admin_management_change.winfo_screenheight() - 400) / 2))
    root_admin_management_change.title('管理员-管理-修改')

    admin_windows(root_admin_management_change)
    main_frame_admin_management_window_windows(root_admin_management_change)
    main_frame_admin_management_command_change_windows(root_admin_management_change)


#管理员-管理

#管理员-管理-窗口
def main_frame_admin_management_window_windows(root):
    global main_frame_admin_management_window
    main_frame_admin_management_window = Frame(root)

    main_frame_admin_management_window_sb1 = Scrollbar(main_frame_admin_management_window)
    main_frame_admin_management_window_sb1.pack(side=RIGHT, fill=Y)

    main_frame_admin_management_window_lb1 = Listbox(main_frame_admin_management_window, yscrollcommand=main_frame_admin_management_window_sb1.set, width=40, height=19,font=('微软雅黑', 11))
    for item in read_item('data.txt', 'r'):
        main_frame_admin_management_window_lb1.insert(END, str(item))
    main_frame_admin_management_window_lb1.pack(side=LEFT, fill=BOTH)

    main_frame_admin_management_window_sb1.config(command=main_frame_admin_management_window_lb1.yview)

    main_frame_admin_management_window.grid(row=1, column=0, rowspan=2)


def main_frame_admin_management_command_windows(root):
    global main_frame_admin_management_command
    main_frame_admin_management_command = Frame(root)

    main_frame_admin_management_command_b1 = Button(main_frame_admin_management_command, text='增加', command=admin_management_add).grid(row=0, column=0)
    main_frame_admin_management_command_b2 = Button(main_frame_admin_management_command, text='删除', command=admin_management_delete).grid(row=1, column=0)
    main_frame_admin_management_command_b3 = Button(main_frame_admin_management_command, text='修改', command=admin_management_change).grid(row=2, column=0)

    main_frame_admin_management_command.grid(row=1, column=1, rowspan=2)


#管理员-管理-根
def admin_management():
    destroy_root()
    root_admin_management = Tk()
    add_root_to_rootlist(root_admin_management)
    root_admin_management.geometry("%dx%d+%d+%d" % (800, 400, (root_admin_management.winfo_screenwidth() - 800) / 2, (root_admin_management.winfo_screenheight() - 400) / 2))
    root_admin_management.title('管理员-管理')

    admin_windows(root_admin_management)
    #main_frame_admin_management_command_windows(root_admin_management)
    main_frame_admin_management_window_windows(root_admin_management)






#管理员

#管理员-窗口
def admin_windows(root):
    global main_frame_admin
    main_frame_admin = Frame(root)

    '''main_frame_admin_b1 = Button(main_frame_admin, text="管理套餐内容", command=admin_management)
    main_frame_admin_b1.grid(row=0, column=1)
    main_frame_admin_b2 = Button(main_frame_admin, text="查询用户信息", command=admin_userinfo)
    main_frame_admin_b2.grid(row=0, column=2)'''


    main_frame_admin_menubar = Menu(root, font=('微软雅黑', 14))
    main_frame_admin_management_menu = Menu(main_frame_admin_menubar, tearoff=False)
    main_frame_admin_management_menu.add_command(label="增加", command=admin_management_add, font=('微软雅黑', 12))
    main_frame_admin_management_menu.add_separator()
    main_frame_admin_management_menu.add_command(label="删除", command=admin_management_delete, font=('微软雅黑', 12))
    main_frame_admin_management_menu.add_separator()
    main_frame_admin_management_menu.add_command(label="修改", command=admin_management_change, font=('微软雅黑', 12))
    main_frame_admin_management_menu.add_separator()
    main_frame_admin_menubar.add_cascade(label="管理套餐内容", menu=main_frame_admin_management_menu)

    main_frame_admin_menubar.add_command(label="查询用户信息", command=admin_userinfo)

    main_frame_admin_menubar.add_command(label="用户数据分析", command=admin_userdata)

    main_frame_admin_menubar.add_command(label="注销", command=(lambda: logout_window(root)), font=('微软雅黑', 11))

    root.config(menu=main_frame_admin_menubar)

    main_frame_admin.grid(row=0, column=0)


#管理员-根
def admin():
    destroy_root()

    global root_admin
    root_admin = Tk()
    add_root_to_rootlist(root_admin)
    root_admin.geometry("%dx%d+%d+%d" % (800, 400, (root_admin.winfo_screenwidth() - 800) / 2, (root_admin.winfo_screenheight() - 400) / 2))
    root_admin.title('管理员')

    admin_windows(root_admin)

    mainloop()








#用户-推荐

#用户-推荐-命令
def user_recommand_direct():
    global recommand_list
    recommand_list = auto_recommend(user_name)

    global origin_recommand_list
    origin_recommand_list = copy.deepcopy(recommand_list)

    for each in recommand_list:
        each.append(recommand_list.index(each))
        each[0] = search_item_by_id(each[0])[0]

    user_recommand_show_windows(root_user_recommand_show2, recommand_list)


def user_recommand_show_command():
    user_choice = str(user_name) + ' ' + str(origin_recommand_list[user_recommand_command_v.get()][0])

    if save_user_choice(user_choice) == "file_error":
        user_recommand_show_v.set('保存错误')
    else:
        user_recommand_show_v.set('保存成功')


def user_recommand_command():








        user_recommand_show_windows(root_user_recommand_show1, recommand_list)

#用户-推荐-列表

#用户-推荐-列表-窗口
def user_recommand_show_windows(root, list1):
    global main_frame_user_recommand_show
    main_frame_user_recommand_show = Frame(root)

    main_frame_user_recommand_show_l1 = Label(main_frame_user_recommand_show, text='             ', height=2).grid(row=0, column=0, rowspan=9)
    main_frame_user_recommand_show_l2 = Label(main_frame_user_recommand_show, text='以下为系统为您自动筛选出的适合您的套餐：\n (套餐名，月资费，通话时长，流量，宽带)   ', font=('微软雅黑', 10), height=3).grid(row=0, column=1, sticky=W)


    for package, value, i in list1:
        b = Radiobutton(main_frame_user_recommand_show, text=package, variable=user_recommand_command_v, value=i, anchor=W, font=('微软雅黑', 11), height=2).grid(row=i+1, column=1, sticky=W)
        if i >= 4:
            break

    root_user_recommand_show_l6 = Label(main_frame_user_recommand_show, textvariable=user_recommand_show_v, font=('微软雅黑', 10)).grid(row=8, column=1)

    root_user_recommand_show_b1 = Button(main_frame_user_recommand_show, text='确定', command=user_recommand_show_command).grid(row=7, column=1)

    main_frame_user_recommand_show.grid(row=1, column=1)


# 用户-推荐-列表-根
def user_recommand_show1():
    global user_recommand_command_v
    user_recommand_command_v = IntVar()
    user_recommand_command_v.set(0)

    global user_recommand_show_v
    user_recommand_show_v = StringVar()

    global recommand_cost
    recommand_cost = main_frame_user_recommand_input_e1.get()
    global recommand_communication_length
    recommand_communication_length = main_frame_user_recommand_input_e2.get()
    global recommand_data
    recommand_data = main_frame_user_recommand_input_e3.get()
    global recommand_internet
    recommand_internet = main_frame_user_recommand_input_e4.get()
    print(recommand_cost, recommand_communication_length, recommand_data, recommand_internet)

    if recommand_data == '':
        recommand_data = 0
    if recommand_internet == '':
        recommand_internet = 0
    data_SI = main_frame_user_recommand_input_c1.get()
    internet_SI = main_frame_user_recommand_input_c2.get()

    if judge_digtal(str(recommand_cost)) == "请输入大于0纯数字" or judge_digtal(str(recommand_communication_length)) == "请输入大于0纯数字" or judge_digtal(str(recommand_data)) == "请输入大于0纯数字" or judge_digtal(str(recommand_internet)) == "请输入大于0纯数字":
        user_recommand_input_v.set("请输入大于等于0纯数字")
    else:
        recommand_data = str(recommand_data) + str(data_SI)
        recommand_internet = str(recommand_internet) + str(internet_SI)

        print(recommand_cost, recommand_communication_length, recommand_data, recommand_internet)

        global info
        info = str(recommand_cost) + ' ' + str(recommand_communication_length) + ' ' + str(recommand_data) + ' ' + str(recommand_internet)

        user_log = user_name + ' ' + info
        if receive_user_log(user_log) == "file_error":
            user_recommand_input_v.set('数据保存错误')
        else:
            user_recommand_input_v.set('数据保存成功')

        global recommand_list
        recommand_list = recommend_package(info)

        if recommand_list == "input_or_file_error":
            user_recommand_input_v.set('输入错误')

        global origin_recommand_list
        origin_recommand_list = copy.deepcopy(recommand_list)

        for each in recommand_list:
            each.append(recommand_list.index(each))
            each[0] = search_item_by_id(each[0])[0]

    if recommand_cost == '':
        recommand_cost = 0
    if recommand_communication_length == '':
        recommand_communication_length = 0

    destroy_root()
    global root_user_recommand_show1
    root_user_recommand_show1 = Tk()
    add_root_to_rootlist(root_user_recommand_show1)
    root_user_recommand_show1.geometry("%dx%d+%d+%d" % (800, 400, (root_user_recommand_show1.winfo_screenwidth() - 800) / 2, (root_user_recommand_show1.winfo_screenheight() - 400) / 2))
    root_user_recommand_show1.title('用户-推荐')



    user_windows(root_user_recommand_show1)
    user_recommand_input_windows(root_user_recommand_show1)
    user_recommand_command()
    #user_recommand_show_windows(root_user_recommand_show1, recommand_list)


def user_recommand_show2():
    destroy_root()
    global root_user_recommand_show2
    root_user_recommand_show2 = Tk()
    add_root_to_rootlist(root_user_recommand_show2)
    root_user_recommand_show2.geometry("%dx%d+%d+%d" % (800, 400, (root_user_recommand_show2.winfo_screenwidth() - 800) / 2, (root_user_recommand_show2.winfo_screenheight() - 400) / 2))
    root_user_recommand_show2.title('用户-推荐')

    global user_recommand_command_v
    user_recommand_command_v = IntVar()
    user_recommand_command_v.set(0)

    global user_recommand_show_v
    user_recommand_show_v = StringVar()

    user_windows(root_user_recommand_show2)
    user_recommand_input_windows(root_user_recommand_show2)
    user_recommand_direct()
    #user_recommand_show_windows(root_user_recommand_show2, recommand_list)

#用户-推荐-窗口
def user_recommand_input_windows(root):
    global main_frame_user_recommand_input
    main_frame_user_recommand_input = Frame(root)

    main_frame_user_recommand_input_l1 = Label(main_frame_user_recommand_input, text='月资费', font=('微软雅黑', 11), height=2).grid(row=4, column=0)
    main_frame_user_recommand_input_l2 = Label(main_frame_user_recommand_input, text='通话时长', font=('微软雅黑', 11), height=2).grid(row=5, column=0)
    main_frame_user_recommand_input_l3 = Label(main_frame_user_recommand_input, text='4G流量', font=('微软雅黑', 11), height=2).grid(row=6, column=0)
    main_frame_user_recommand_input_l4 = Label(main_frame_user_recommand_input, text='宽带带宽', font=('微软雅黑', 11), height=2).grid(row=7, column=0)
    main_frame_user_recommand_input_l5 = Label(main_frame_user_recommand_input, text='请输入意向套餐相关内容（所有输入需为整数）:', font=('微软雅黑', 11), height=1).grid(row=3, column=0, columnspan=4)
    main_frame_user_recommand_input_l6 = Label(main_frame_user_recommand_input, textvariable=user_recommand_input_v, font=('微软雅黑', 10), height=2).grid(row=9, column=0)
    main_frame_user_recommand_input_l7 = Label(main_frame_user_recommand_input, text='根据消费历史推荐：', font=('微软雅黑', 11), height=4).grid(row=0, column=0)
    main_frame_user_recommand_input_l8 = Label(main_frame_user_recommand_input, text='根据具体需求推荐：', font=('微软雅黑', 11), height=2).grid(row=2, column=0)
    main_frame_user_recommand_input_l9 = Label(main_frame_user_recommand_input, text='        ', height=2).grid(row=0, column=3, rowspan=9)

    global main_frame_user_recommand_input_e1
    main_frame_user_recommand_input_e1 = Entry(main_frame_user_recommand_input, width=10)
    main_frame_user_recommand_input_e1.grid(row=4, column=1)
    global main_frame_user_recommand_input_e2
    main_frame_user_recommand_input_e2 = Entry(main_frame_user_recommand_input, width=10)
    main_frame_user_recommand_input_e2.grid(row=5, column=1)
    global main_frame_user_recommand_input_e3
    main_frame_user_recommand_input_e3 = Entry(main_frame_user_recommand_input, width=10)
    main_frame_user_recommand_input_e3.grid(row=6, column=1)
    global main_frame_user_recommand_input_e4
    main_frame_user_recommand_input_e4 = Entry(main_frame_user_recommand_input, width=10)
    main_frame_user_recommand_input_e4.grid(row=7, column=1)

    global main_frame_user_recommand_input_c1
    main_frame_user_recommand_input_c1 = ttk.Combobox(main_frame_user_recommand_input, width=2, state='readonly')
    main_frame_user_recommand_input_c1['values'] = ('M', 'G')
    main_frame_user_recommand_input_c1.current(0)
    main_frame_user_recommand_input_c1.grid(row=6, column=2)
    global main_frame_user_recommand_input_c2
    main_frame_user_recommand_input_c2 = ttk.Combobox(main_frame_user_recommand_input, width=2, state='readonly')
    main_frame_user_recommand_input_c2['values'] = ('M')
    main_frame_user_recommand_input_c2.current(0)
    main_frame_user_recommand_input_c2.grid(row=7, column=2)

    main_frame_user_recommand_input_b1 = Button(main_frame_user_recommand_input, text='确定', command=user_recommand_show1).grid(row=4, column=4, rowspan=4)
    main_frame_user_recommand_input_b2 = Button(main_frame_user_recommand_input, text='一键推荐', command=user_recommand_show2).grid(row=0, column=4)

    main_frame_user_recommand_input.grid(row=1, column=0)


#用户-推荐=根
def user_recommand():
    destroy_root()
    global root_user_recommand
    root_user_recommand = Tk()
    add_root_to_rootlist(root_user_recommand)
    root_user_recommand.geometry("%dx%d+%d+%d" % (800, 400, (root_user_recommand.winfo_screenwidth() - 800) / 2, (root_user_recommand.winfo_screenheight() - 400) / 2))
    root_user_recommand.title('用户-推荐')

    global user_recommand_input_v
    user_recommand_input_v = StringVar()



    user_windows(root_user_recommand)
    user_recommand_input_windows(root_user_recommand)



#用户-个人信息


#用户-个人信息-往期记录

#用户-个人信息-往期记录-窗口
def user_selfinfo_log_windows(root):
    global main_frame_user_selfinfo_log
    main_frame_user_selfinfo_log = Frame(root)

    main_frame_user_selfinfo_log_l1 = Label(main_frame_user_selfinfo_log, text='近六个月的消费情况（从今至前）：', font=('微软雅黑', 11), height=2).grid(row=0, column=0)
    main_frame_user_selfinfo_log_l2 = Label(main_frame_user_selfinfo_log, text='月资费 通话时长 流量 宽带', font=('微软雅黑', 10), height=2).grid(row=1, column=0)
    main_frame_user_selfinfo_log_l3 = Label(main_frame_user_selfinfo_log, textvariable=user_selfinfo_log_v1, font=('微软雅黑', 10), height=2).grid(row=2, column=0)
    main_frame_user_selfinfo_log_l4 = Label(main_frame_user_selfinfo_log, textvariable=user_selfinfo_log_v2, font=('微软雅黑', 10), height=2).grid(row=3, column=0)
    main_frame_user_selfinfo_log_l5 = Label(main_frame_user_selfinfo_log, textvariable=user_selfinfo_log_v3, font=('微软雅黑', 10), height=2).grid(row=4, column=0)
    main_frame_user_selfinfo_log_l6 = Label(main_frame_user_selfinfo_log, textvariable=user_selfinfo_log_v4, font=('微软雅黑', 10), height=2).grid(row=5, column=0)
    main_frame_user_selfinfo_log_l7 = Label(main_frame_user_selfinfo_log, textvariable=user_selfinfo_log_v5, font=('微软雅黑', 10), height=2).grid(row=6, column=0)
    main_frame_user_selfinfo_log_l8 = Label(main_frame_user_selfinfo_log, textvariable=user_selfinfo_log_v6, font=('微软雅黑', 10), height=2).grid(row=7, column=0)

    info_list = []
    for i in range(6):
        info = ''
        for j in range(4):
            info = info + read_user_history(user_name)[i][j] + ' '
        info_list.append(info)

    user_selfinfo_log_v1.set(info_list[0])
    user_selfinfo_log_v2.set(info_list[1])
    user_selfinfo_log_v3.set(info_list[2])
    user_selfinfo_log_v4.set(info_list[3])
    user_selfinfo_log_v5.set(info_list[4])
    user_selfinfo_log_v6.set(info_list[5])

    main_frame_user_selfinfo_log.grid(row=0, column=0)


#用户-个人信息-往期记录-根
def user_selfinfo_log():
    destroy_root()
    global root_user_selfinfo_log
    root_user_selfinfo_log= Tk()
    add_root_to_rootlist(root_user_selfinfo_log)
    root_user_selfinfo_log.geometry("%dx%d+%d+%d" % (800, 400, (root_user_selfinfo_log.winfo_screenwidth() - 800) / 2, (root_user_selfinfo_log.winfo_screenheight() - 400) / 2))
    root_user_selfinfo_log.title('用户-个人信息-往期记录')

    global user_selfinfo_log_v1
    user_selfinfo_log_v1 = StringVar()
    global user_selfinfo_log_v2
    user_selfinfo_log_v2 = StringVar()
    global user_selfinfo_log_v3
    user_selfinfo_log_v3 = StringVar()
    global user_selfinfo_log_v4
    user_selfinfo_log_v4 = StringVar()
    global user_selfinfo_log_v5
    user_selfinfo_log_v5 = StringVar()
    global user_selfinfo_log_v6
    user_selfinfo_log_v6 = StringVar()

    user_windows(root_user_selfinfo_log)
    user_selfinfo_log_windows(root_user_selfinfo_log)


#用户-个人信息-当前套餐

#用户-个人信息-当前套餐-窗口
def user_selfinfo_currentpackage_windows(root):
    global main_frame_user_selfinfo_currentpackage
    main_frame_user_selfinfo_currentpackage = Frame(root)

    main_frame_user_selfinfo_currentpackage_l1 = Label(main_frame_user_selfinfo_currentpackage, text='当前套餐：', font=('微软雅黑', 11), height=2).grid(row=0, column=0)
    main_frame_user_selfinfo_currentpackage_l2 = Label(main_frame_user_selfinfo_currentpackage, textvariable=user_selfinfo_currentpackage_v, font=('微软雅黑', 10), height=3).grid(row=1, column=0)
    user_selfinfo_currentpackage_v.set(read_user_choice(user_name)[0])

    main_frame_user_selfinfo_currentpackage_b2 = Button(main_frame_user_selfinfo_currentpackage, text='修改套餐', command=user_recommand, font=('微软雅黑', 11)).grid(row=2, column=0)

    main_frame_user_selfinfo_currentpackage.grid(row=0, column=0)


#用户-个人信息-当前套餐-根
def user_selfinfo_currentpackage():
    destroy_root()
    global root_user_selfinfo_currentpackage
    root_user_selfinfo_currentpackage = Tk()
    add_root_to_rootlist(root_user_selfinfo_currentpackage)
    root_user_selfinfo_currentpackage.geometry("%dx%d+%d+%d" % (800, 400, (root_user_selfinfo_currentpackage.winfo_screenwidth() - 800) / 2, (root_user_selfinfo_currentpackage.winfo_screenheight() - 400) / 2))
    root_user_selfinfo_currentpackage.title('用户-个人信息-当前套餐')

    global user_selfinfo_currentpackage_v
    user_selfinfo_currentpackage_v = StringVar()

    #user_selfinfo_windows(root_user_selfinfo_currentpackage)
    user_windows(root_user_selfinfo_currentpackage)
    user_selfinfo_currentpackage_windows(root_user_selfinfo_currentpackage)


#用户-个人信息-窗口
def user_selfinfo_windows(root):
    global main_frame_user_selfinfo
    main_frame_user_selfinfo = Frame(root)

    main_frame_user_selfinfo_b1 = Button(main_frame_user_selfinfo, text='当前套餐信息', command=user_selfinfo_currentpackage).grid(row=0, column=0)
    main_frame_user_selfinfo_b2 = Button(main_frame_user_selfinfo, text='往期消费记录', command=user_selfinfo_log).grid(row=0, column=1)

    main_frame_user_selfinfo.grid(row=0, column=0)



#用户-个人信息-根
def user_selfinfo():
    destroy_root()
    global root_user_selfinfo
    root_user_selfinfo = Tk()
    add_root_to_rootlist(root_user_selfinfo)
    root_user_selfinfo.geometry("%dx%d+%d+%d" % (800, 400, (root_user_selfinfo.winfo_screenwidth() - 800) / 2, (root_user_selfinfo.winfo_screenheight() - 400) / 2))
    root_user_selfinfo.title('用户-个人信息')

    #user_selfinfo_windows(root_user_selfinfo)
    user_windows(root_user_selfinfo)

#用户

#用户-窗口
def user_windows(root):
    global main_frame_user
    main_frame_user = Frame(root)

    '''main_frame_user_b1 = Button(main_frame_user, text="套餐推荐", command=user_recommand)
    main_frame_user_b1.grid(row=0, column=1)
    main_frame_user_b2 = Button(main_frame_user, text="个人信息", command=user_selfinfo)
    main_frame_user_b2.grid(row=0, column=2)'''

    main_frame_user_menubar = Menu(root, font=('微软雅黑', 11))


    main_frame_user_menubar.add_command(label="套餐推荐", command=user_recommand, font=('微软雅黑', 11))

    main_frame_user_selfinfo_menu = Menu(main_frame_user_menubar, tearoff=False)
    main_frame_user_selfinfo_menu.add_command(label="当前套餐信息", command=user_selfinfo_currentpackage, font=('微软雅黑', 11))
    main_frame_user_selfinfo_menu.add_separator()
    main_frame_user_selfinfo_menu.add_command(label="往期消费记录", command=user_selfinfo_log, font=('微软雅黑', 11))
    main_frame_user_selfinfo_menu.add_separator()
    main_frame_user_menubar.add_cascade(label="管理套餐内容", menu=main_frame_user_selfinfo_menu, font=('微软雅黑', 11))

    main_frame_user_menubar.add_command(label="注销", command=(lambda: logout_window(root)), font=('微软雅黑', 11))



    root.config(menu=main_frame_user_menubar)

    main_frame_user.grid(row=0, column=0)


#用户-根
def user():
    destroy_root()
    global root_user
    root_user = Tk()
    add_root_to_rootlist(root_user)
    root_user.geometry("%dx%d+%d+%d" % (800, 400, (root_user.winfo_screenwidth() - 800) / 2, (root_user.winfo_screenheight() - 400) / 2))
    root_user.title('用户')

    user_windows(root_user)


#注销弹窗
def logout_window(root):
    logout_window_t1 = Toplevel(root)
    logout_window_t1.title('注销')
    logout_window_t1.geometry("%dx%d+%d+%d" % (150, 100, (logout_window_t1.winfo_screenwidth() - 150) / 2, (logout_window_t1.winfo_screenheight() - 100) / 2))

    logout_window_t1_frame = Frame(logout_window_t1)
    logout_window_l1 = Label(logout_window_t1_frame, text='确认要注销吗？', font=('微软雅黑', 12), height=2).grid(row=0, column=0, columnspan=2)

    logout_window_b1 = Button(logout_window_t1_frame, text='确定', command=login_window, font=('微软雅黑', 11)).grid(row=1, column=0)
    logout_window_b2 = Button(logout_window_t1_frame, text='取消', command=logout_window_t1.destroy, font=('微软雅黑', 11)).grid(row=1, column=1)

    logout_window_t1_frame.pack()



def sign():
    print(2)
    global user_name
    user_name = main_frame_e1.get()
    global password
    password = main_frame_e2.get()
    if login(user_name, password) == "id_not_found":
        login_v.set('用户名不存在')
    elif login(user_name, password) == "password_error":
        login_v.set('密码错误')
    elif login(user_name, password) == "login_success_with_admin":
        admin()
    else:
        user()


def login_window():
    print('1')

    destroy_root()
    global root_main_frame
    root_main_frame = Tk()
    add_root_to_rootlist(root_main_frame)
    root_main_frame.geometry("%dx%d+%d+%d" % (380, 240, (root_main_frame.winfo_screenwidth() - 380) / 2, (root_main_frame.winfo_screenheight() - 240) / 2))
    root_main_frame.title('用户登录')

    global login_v
    login_v = StringVar()

    global main_frame
    main_frame = Frame(root_main_frame)

    main_frame_l1 = Label(main_frame, text='用户登录', font=('微软雅黑', 20), height=2).grid(row=0, column=0, columnspan=2, sticky=W + E)
    main_frame_l2 = Label(main_frame, text='用户名', font=('微软雅黑', 14)).grid(row=2, column=0)
    main_frame_l3 = Label(main_frame, text='密码', font=('微软雅黑', 14)).grid(row=3, column=0)
    main_frame_l5 = Label(main_frame, text='', height=1).grid(row=4, column=0, columnspan=2, sticky=W + E)
    main_frame_l4 = Label(main_frame, textvariable=login_v, font=('微软雅黑', 10)).grid(row=6, column=0, columnspan=2, sticky=W + E)

    global main_frame_e1
    main_frame_e1 = Entry(main_frame)
    main_frame_e1.grid(row=2, column=1)
    global main_frame_e2
    main_frame_e2 = Entry(main_frame)
    main_frame_e2['show'] = '*'
    main_frame_e2.grid(row=3, column=1)

    main_frame_b1 = Button(main_frame, text='登录', command=sign, font=('微软雅黑', 14), width=8).grid(row=5, column=0, columnspan=2)

    main_frame.pack()



def welcome():
    destroy_root()
    global root
    root = Tk()
    add_root_to_rootlist(root)
    root.geometry("%dx%d+%d+%d" % (380, 120, (root.winfo_screenwidth() - 380) / 2, (root.winfo_screenheight() - 120) / 2))
    root.title('欢迎使用本程序')

    welcome_l1 = Label(root, text='欢迎使用电信套餐综合管理系统', font=('微软雅黑', 20), height=2).grid(row=0, column=0, sticky=W + E)

    welcome_b1 = Button(root, text='下一步', command=login_window, font=('微软雅黑', 14), width=8).grid(row=1, column=0)

    mainloop()


welcome()

