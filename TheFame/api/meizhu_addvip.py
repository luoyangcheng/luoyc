import sys
import os
sys.path.append('../TheFame/common/')
import logger, Open_Excel


def addvip(session, hotel, name, mobile, vipInfoId, gender, share, areaCode, vipLevelName):
    global result  # 设置全局变量
    data = {'hotel': hotel, 'name': name, 'mobile': mobile, "vipInfoId": vipInfoId, "gender": gender, "share": share, "areaCode": areaCode, "vipLevelName": vipLevelName}
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
    Test_data = []
    for i in range(1, 10):
        one_data = Open_Excel.read_excel(excel_path, '添加会员', i)
        Test_data.append(one_data)
    actual = []
    for hotel, name, mobile, vipInfoId, gender, share, areaCode, vipLevelName, expected in zip(Test_data[0], Test_data[1], Test_data[2], Test_data[3], Test_data[4], Test_data[5], Test_data[6], Test_data[7], Test_data[8]):
        addvip(session, hotel, name, mobile, vipInfoId, gender, share, areaCode, vipLevelName)
        if result == expected:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    Open_Excel.write_excel(excel_path, '添加会员', actual)
