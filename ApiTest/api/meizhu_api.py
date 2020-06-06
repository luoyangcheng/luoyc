import sys
sys.path.append('../ApiTest/common/')
import logger, Open_Excel, TestRequests
from configparser import ConfigParser


def meizhu(r_type, parameter_type, sheet, url, field=[], valu=[]):
    cfg = ConfigParser()
    cfg.read('../ApiTest/common/config.ini')
    ip = (cfg.get('server', 'ip'))
    port = (cfg.get('server', 'port'))
    excel_path = (cfg.get('excel', 'excel_path'))
    x = TestRequests.Test_Requests()
    log = logger.Log()
    Open_Excel.update_excel(excel_path, sheet)
    Test_data = Open_Excel.read_excel_row(excel_path, sheet, field=field, valu=valu)
    expect, actual = [], []
    for i in Test_data:
        if parameter_type == 'dict':
            result = x.run_main(r_type, url=ip + ':' + port + url, data=i)
        elif parameter_type == 'json':
            result = x.run_main(r_type, url=ip + ':' + port + url, json=i)
        else:
            print('传参类型错误')
        result = result.content.decode('utf-8')
        expected = i['expect']
        if result == expected:
            log.info(sheet + '--' + result)
            actual.append(result)
            expect.append(expected)
        else:
            log.error(sheet + '--' + result)
            actual.append(result)
            expect.append(expected)
    Open_Excel.write_excel(excel_path, sheet, actual)
    return expect, actual
