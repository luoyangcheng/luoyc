import sys
import os
sys.path.append('../ApiTest/common/')
import logger, Open_Excel, TestRequests


def addvip():
    x = TestRequests.Test_Requests()
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../ApiTest/case/case.xlsx"
    sheet = '添加会员'
    Open_Excel.update_excel(excel_path, sheet)
    Test_data = []
    for i in range(1, 10):
        one_data = Open_Excel.read_excel(excel_path, sheet, i)
        Test_data.append(one_data)
    actual = []
    for hotel, name, mobile, vipInfoId, gender, share, areaCode, vipLevelName, expected in zip(Test_data[0], Test_data[1], Test_data[2], Test_data[3], Test_data[4], Test_data[5], Test_data[6], Test_data[7], Test_data[8]):
        result = x.run_main('post', url='http://www.meizhuyun.com/Home/Customer/addVip', data={'hotel': hotel, 'name': name, 'mobile': mobile, 'vipInfoId': vipInfoId, 'gender': gender, 'share': share, 'areaCode': areaCode, 'vipLevelName': vipLevelName})
        result = result.content.decode('utf-8')
        # print(result)
        if result == expected:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    Open_Excel.write_excel(excel_path, sheet, actual)
    return Test_data[8], actual
