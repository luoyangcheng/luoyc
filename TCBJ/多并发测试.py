import threading
import requests


def ll(i):
    url1 = "https://wx-test1.by-health.com/scrmv2/liteactivity/xrlb/getPrizeMsg"
    url2 = 'https://wx-test1.by-health.com/scrmv2/marketing/consumerLottery'
    data1 = {"phone": i, "validateCode": "7474", "loginSource": "xrlb", "sourceFrom": "新人礼包"}
    data2 = {"activityId": "116375", "lotteryMemberId": "51330315", "lotteryType": "task_lottery", "identityType": "WECHAT_YYJ", "channelType": 11, "tag": "xrhb"}
    resp = requests.post(url1, json=data1)
    status = resp.status_code
    seTime = resp.elapsed.microseconds
    if status == 500:
        print(i)
        print(resp.content.decode('utf-8'))
    # print(i, '请求状态:', status, '请求耗时：', seTime / 1000000)


T = []
for i in range(18802094378, 18802094428):
    t1 = threading.Thread(target=ll, args=(i,))
    T.append(t1)

if __name__ == '__main__':
    for i in T:
        i.setDaemon(True)
        i.start()
    for j in T:
        j.join()
