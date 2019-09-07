# 新线程执行的代码:
#coding=utf-8
import threading
from time import ctime,sleep

# def music(func):
#     for i in range(2):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print ("I was at the %s! %s" %(func,ctime()))
#         sleep(5)
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#     t.join()
#
#     print ("all over %s" %ctime())

from Test.meizhu_login import login
import threading

t1 = threading.Thread(target=login.ll ,args=('18802094078','qq111111','86'))
t2 = threading.Thread(target=login.ll ,args=('13480251015','111111b','86'))


if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()