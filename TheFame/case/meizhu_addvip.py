import sys
import os
sys.path.append('../TheFame/common/')
import logger


def addvip(session, hotel, name, mobile, vipInfoId, gender, share, areaCode,
           vipLevelName):
    global result  # 设置全局变量
    data = {
        'hotel': hotel,
        'name': name,
        'mobile': mobile,
        "vipInfoId": vipInfoId,
        "gender": gender,
        "share": share,
        "areaCode": areaCode,
        "vipLevelName": vipLevelName
    }
    addvip_url = "http://www.meizhuyun.com/Home/Customer/addVip"
    result = session.post(addvip_url, data)
    result = result.content.decode('utf-8')


def test_addvip(session):
    # 测试美住添加vip
    addvip(session, '277', 'luoyc', '18802094078', '1', '0', '1', ' 86',
           '黄金VIP')
    filename = os.path.basename(__file__)
    log = logger.Log()
    log.info(filename + '--' + result)
    log.error(filename + '--' + result)
