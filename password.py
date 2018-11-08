#import zlib
#s = b'123456'
#print(str(zlib.crc32(s)))

'''def add_to_list(content):
    try:
        with open('login.txt', 'a+') as f:
            f.write(content+'\n')
    except FileNotFoundError:
        return "file_error"
    else:
        return "save_success"

def read_login(route, way):
    try:
        with open(route, way) as f:
            data = f.login()
    except FileNotFoundError or IOError:
            return "file_error"
    else:
            return data
'''


import file_process
import zlib

datas = file_process.read_item('login.txt','r')
i = 0
for data in datas:
    item = data.split()
    password = item[1]
    password = str(zlib.crc32(bytes(password,"utf-8")))
    datas[i] = item[0] + ' ' + password + ' ' + item[2] + '\n'
    i += 1
print(file_process.write_to_file('login.txt', datas, 'w+'))