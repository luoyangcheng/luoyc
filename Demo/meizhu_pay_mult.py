from Test.meizhu_pay import coupons
import threading

t1 = threading.Thread(
    target=coupons.bc, args=('17094101202', '111111b', '86', '309'))
t2 = threading.Thread(
    target=coupons.bc, args=('18802094078', 'qq111111', '86', '8'))

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
