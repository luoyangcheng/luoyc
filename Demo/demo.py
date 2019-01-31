import hashlib
import os


def demo(x, y):
    x = x
    print(x > y + 11 + (x - y - 11) * 0.032)


def md5(data):
    a = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    print(a)



# demo(22.04, 10)
# md5("qq111111")
maketxt("C:/meizhu.txt")
