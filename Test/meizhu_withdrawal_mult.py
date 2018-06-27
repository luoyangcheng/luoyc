from Test.meizhu_withdrawal2 import withdrawal2
import threading

t1 = threading.Thread(target=withdrawal2.bc, args=('18802094078', 'qq111111', '86', '309', '0.01', '917498'))
t2 = threading.Thread(target=withdrawal2.bc, args=('18802094078', 'qq111111', '86', '309', '0.01', '917498'))

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
