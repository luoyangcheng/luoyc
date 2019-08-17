import sys
import os
sys.path.append('../TheFame/common/')
import logger, Open_Excel


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
    try:
        addvip_url = "http://www.meizhuyun.com/Home/Customer/addVip"
        result = session.post(addvip_url, data)
    except Exception as e:
        print('接口请求出错！', e)
    else:
        result = result.content.decode('utf-8')
    
    


def test_addvip(session):
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../TheFame/case/case.xlsx"
    hotel = Open_Excel.read_excel(excel_path, '添加会员', 1)
    name = Open_Excel.read_excel(excel_path, '添加会员', 2)
    mobile = Open_Excel.read_excel(excel_path, '添加会员', 3)
    vipInfoId = Open_Excel.read_excel(excel_path, '添加会员', 4)
    gender = Open_Excel.read_excel(excel_path, '添加会员', 5)
    share = Open_Excel.read_excel(excel_path, '添加会员', 6)
    areaCode = Open_Excel.read_excel(excel_path, '添加会员', 7)
    vipLevelName = Open_Excel.read_excel(excel_path, '添加会员', 8)
    expected = Open_Excel.read_excel(excel_path, '添加会员', 9)
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
    Open_Excel.write_excel(excel_path, '添加会员', actual)
