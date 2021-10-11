import sys
sys.path.append('./')
import json
import common
from common.logger import Log
from common.Open_Excel import read_excel_row, write_excel, update_excel
from common.up_data import up_excel
from common.TestRequests import Test_Requests
from configparser import ConfigParser


def yyy(r_type, parameter_type, sheet, row_name, field=[], valu=[]):
    global result
    cfg = ConfigParser()
    cfg.read('../ApiTest/common/config.ini')
    ip = (cfg.get('server', 'ip'))
    port = (cfg.get('server', 'port'))
    excel_path = (cfg.get('excel', 'excel_path'))
    x = Test_Requests()
    log = Log()
    update_excel(excel_path, sheet)
    Test_data = read_excel_row(excel_path, sheet, row_name, field=field, valu=valu)
    log.info(type(Test_data))
    api_url = Test_data[0]['url']
    if parameter_type == 'webForms':
        result = x.run_main(r_type, url=ip + api_url, data=Test_data[0])
    elif parameter_type == 'json':
        j = Test_data[0]['data']
        k = json.loads(j)
        # log.info(j)
        result = x.run_main(r_type, url=ip + api_url, json=k)
        # log.info(result)
    else:
        print('传参类型错误')
    result = str(result.status_code)
    expected = Test_data[0]['expect']
    write_excel(excel_path, sheet, result, row_name)
    return expected, result
