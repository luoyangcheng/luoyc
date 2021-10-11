import time
from common.random_name import random_full_name


def up_excel(i):
    nowTime = int(time.time())  # 获取当前时间戳
    mobile = "188" + str(nowTime)[-8:]  # 取时间戳后8位
    if i == "{mobile}":  # 自定义变量，可根据自己需求添加
        i = mobile
    elif i == "{email}":
        i = str(nowTime)[-8:] + '@qq.com'
    elif i is None:
        i = ''
    elif i == '{name}':
        i = random_full_name()
    return i
