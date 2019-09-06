from meizhu_login import login
import threading


def addroom(hotel, name, room, price, charityPrice, rooms, session):
    data = {
        'hotel': hotel,
        'name': name,
        'room': room,
        'price': price,
        'charityPrice': charityPrice,
        'rooms': rooms
    }
    addroom_url = "http://192.168.3.19:8090/Home/Room/editRoom"
    resp = session.post(addroom_url, data)
    print(resp.content.decode('utf-8'))


session = login.ll('18802094078', 'qq111111', '86')
t1 = threading.Thread(
    target=addroom,
    args=
    ('595', '测试', '698', '100', '1',
     '[{"id":2809,"name":"101"},{"id":2810,"name":"102"},{"id":2811,"name":"103"},{"id":2812,"name":"104"},{"id":0,"name":"105"}]',
     session))
t2 = threading.Thread(
    target=addroom,
    args=
    ('595', '测试', '698', '100', '1',
     '[{"id":2809,"name":"101"},{"id":2810,"name":"102"},{"id":2811,"name":"103"},{"id":2812,"name":"104"},{"id":0,"name":"105"}]',
     session))

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
