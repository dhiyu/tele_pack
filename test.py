from tkinter import *

root = Tk()


def call_add_window():
    print('1')
    l1 = Label(root, text='d1').grid(row=1, column=0)


def call_search_window():
    print('2')
    l2 = Label(root, text='d2').grid(row=1, column=0)


def call_sign_window():
    print('3')


def call_change_window():
    print('4')


def call_delete_window():
    print('5')


def call_show_window():
    print('6')


def call_save_window():
    print('7')


main_frame = Frame(root).grid(row=1, column=0)

b1 = Button(root, text="新增", command=call_add_window()).grid(row=0, column=0)
b2 = Button(root, text="搜索", command=call_search_window()).grid(row=0, column=1)
b3 = Button(root, text="注册/注销", command=call_sign_window()).grid(row=0, column=2)
b4 = Button(root, text="修改", command=call_change_window()).grid(row=0, column=3)
b5 = Button(root, text="删除", command=call_delete_window()).grid(row=0, column=4)
b6 = Button(root, text="显示", command=call_show_window()).grid(row=0, column=5)
b7 = Button(root, text="保存", command=call_save_window()).grid(row=0, column=6)


mainloop()