import requests, threading


def n():
    h = {'Referer': 'https://wx-test.by-health.com/web/jkt-mini-h5senior/?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2Mzc5MDQ5ODAsImV4cCI6MTYzODUwOTc4MCwiaXNzIjoiRW1wbG95ZWUiLCJzdWIiOiI1MTMzMjQ1NiJ9.qXgvHJHfqudhXlgNWUq9eVYEuQ1ZKUP0ESbjoWAcSfAgDjAgfQI63LBVj_MbTigkiliqw9cLqhzNBAM49pEdKg'}
    data = {"storeId": "1-1MZNP", "memberId": 51332456, "antifakecode": "3278229827862365", "channelType": 4, "actId": "435", "saleDay": "2021-11-25", "actType": "otherRoadShow"}
    url = 'https://wx-test1.by-health.com/scrmv2/antifakecode/scancodeForPerformance'
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