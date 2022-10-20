import requests, time


def n():
    shijian = int(time.time() * 1000)
    h = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjoib1ROYnBqazJJTjJnemM3MU5DREdKQ0ZrcTRQdyIsImlhdCI6MTY2NjE3MTIzMSwiZXhwIjoxNjY2MjU3NjMxLCJpc3MiOiJ1c2VyIn0.Dgj3PTXVckkpGiFDpF3xQSG3EpvVbtcHSaVAy_XFgWaPGnAshbxEhF0F8EG_mCm6_C9y-FPhk42o9KrG_WjN-g'}
    data = {"totalReward": 1, "saleDate": "2021-10-20", "receiptNo": shijian, "picUrls": ["https://upload-yyj.by-health.com/upload/images/1019173033138.jpg"], "actId": 53, "projectId": 159, "userNo": "4383310988", "items": [{"reward": 1, "reqValue": 1, "productId": 100, "productName": "汤臣倍健多种矿物质片（成人型）（60片）", "upValue": 1}]}
    url = 'https://yygj.by-health.com/guidesales/receiptRecord/h5/add'
    res = requests.post(url, json=data, headers=h, verify=False)
    r = res.content.decode('utf-8')
    print(r)


if __name__ == '__main__':
    n()