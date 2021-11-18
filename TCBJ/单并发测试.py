import requests, threading


def n():
    h = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MzQ1NDM5ODAsImV4cCI6MTYzNDYzMDM4MCwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMzAzMjAifQ.gCnnbG9j2SIzaehSe3bt0WCORkNT_OMogmJoaWF5cgM-dvw_c7mJFXLECb0FHR5UQYdqJTjHBpTlNoocjTMEhg'}
    url = 'https://wx-test1.by-health.com/scrmv2/liteactivity/211028/mainPageMsg?channelType=21&memberId=51330320'
    res = requests.get(url, headers=h)
    r = res.content.decode('utf-8')
    print(r)


t1 = threading.Thread(target=n)
t2 = threading.Thread(target=n)

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
''