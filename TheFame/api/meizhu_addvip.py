import sys
import os
sys.path.append('../TheFame/common/')
import logger, excel


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
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../TheFame/case/case.xlsx"
    hotel = excel.read_excel(excel_path, '添加会员', 1)
    name = excel.read_excel(excel_path, '添加会员', 2)
    mobile = excel.read_excel(excel_path, '添加会员', 3)
    vipInfoId = excel.read_excel(excel_path, '添加会员', 4)
    gender = excel.read_excel(excel_path, '添加会员', 5)
    share = excel.read_excel(excel_path, '添加会员', 6)
    areaCode = excel.read_excel(excel_path, '添加会员', 7)
    vipLevelName = excel.read_excel(excel_path, '添加会员', 8)
    expected = excel.read_excel(excel_path, '添加会员', 9)
    actual = []
    for a, b, c, d, e, f ,h, i, j in zip(hotel, name, mobile, vipInfoId, gender, share,
                          areaCode, vipLevelName, expected):
        addvip(session, a, b, c, d, e, f ,h, i)
        if result == j:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    excel.write_excel(excel_path, '添加会员', actual)
