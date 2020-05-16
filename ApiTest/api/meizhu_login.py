import sys
import os
sys.path.append('../ApiTest/common/')
import logger, Open_Excel, TestRequests


def login():
    x = TestRequests.Test_Requests()
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    excel_path = "../ApiTest/case/case.xlsx"
    sheet = '美住登陆'
    Open_Excel.update_excel(excel_path, sheet)
    Test_data = []
    for i in range(1, 5):
        one_data = Open_Excel.read_excel(excel_path, sheet, i)
        Test_data.append(one_data)
    actual = []
    for mobile, password, areaCode, expected in zip(Test_data[0], Test_data[1], Test_data[2], Test_data[3]):
        result = x.run_main('login', url='http://www.meizhuyun.com/Home/Public/login', data={'mobile': mobile, 'password': password, 'areaCode': areaCode})
        result = result.content.decode('utf-8')
        # print(result)
        if result == expected:
            log.info(filename + '--' + result)
            actual.append(result)
        else:
            log.error(filename + '--' + result)
            actual.append(result)
    Open_Excel.write_excel(excel_path, sheet, actual)
    return Test_data[3], actual
