from Test.booking_coupons import coupons
import threading

t1 = threading.Thread(target=coupons.bc ,args=('18802094078','111111b','86','309','CP180244'))
t2 = threading.Thread(target=coupons.bc ,args=('13480251015','111111b','86','309','CP180244'))


if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()