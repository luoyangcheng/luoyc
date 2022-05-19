import requests, threading


def n():
    h = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NTIyMzA4NTEsImV4cCI6MTY1MjMxNzI1MSwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMzI4MDIifQ.qlqUsZx9DKlVYODqpmWzSaOx1Awu4qftVIx283mYWqEbhIlzWVPXhRVyA7JjB7t96sbD6DS6pCgN37NGs9mpbA'}
    data = {"openId": "o-DCM5TwNG-MCzwZlE2HhQStKQO0", "actId": 135971, "prizeId": 7, "amount": 1}
    url = 'https://yyj-test.by-health.com/scrmv2/liteActivity/exchangePrize'
    res = requests.post(url, json=data, headers=h)
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