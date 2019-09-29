import sys
import os
import time
sys.path.append('../TheFame/common/')
import logger


def max_row(cursor, tb):
    # 获取最大行，也就是多少行测试用例
    cursor.execute("select max(rowid) from %s" % tb)
    row = cursor.fetchall()
    maxrowid = row[0][0]
    return maxrowid


def select_data(cursor, tb, i):
    # 获取某一行的测试用例，并且返回
    global data
    cursor.execute("select * from %s where rowid = %s" % (tb, i))
    data_all = cursor.fetchall()
    data = data_all[0]
    new_data = []
    nowTime = int(time.time())  # 获取当前时间戳
    mobile = "188" + str(nowTime)[-8:]  # 取时间戳后8位
    for i in data:
        if i is None:  #　如果数据库的值为null时，把None替换为空字符串
            i = ""
            new_data.append(i)
        elif i == "{mobile}":  # 自定义变量，可根据自己需求添加
            i = mobile
            new_data.append(i)
        else:
            new_data.append(i)
    return new_data


def update_data(cursor, tb, i, result):
    # 修改 actual、ispass 两个字段,写入日志文件
    filename = os.path.basename(__file__)  # 获取当前文件名
    log = logger.Log()
    # 获取所有字段
    cursor.execute("SELECT * FROM {}".format(tb))
    col_name_list = [tuple[0] for tuple in cursor.description]
    maxcol = len(col_name_list)  # 获取最大列数
    if result == data[maxcol - 3]:
        log.info(filename + '--' + result)
        cursor.execute(
            "update %s set actual = '%s', ispass = 1 where rowid = %s" %
            (tb, result, i))
    else:
        log.error(filename + '--' + result)
        cursor.execute(
            "update %s set actual = '%s', ispass = 0 where rowid = %s" %
            (tb, result, i))


def statistical_data(cursor):
    # 统计错误用例
    fail_num = 0
    tb_num, tb_name = [], []
    # 获取所有表名
    cursor.execute(
        "select name from sqlite_master where type='table' order by name")
    data_all = cursor.fetchall()
    data_all_len = len(data_all)
    # 把表名改成一个list
    for i in range(data_all_len):
        data = data_all[i]
        tb_num.append(data)
    # 查询所有表ispass=0的数据
    for i in tb_num:
        cursor.execute("select count(*) from %s where ispass = '0'" % i)
        fail_count_all = cursor.fetchall()
        fail_count = fail_count_all[0][0]
        if fail_count != 0:
            tb_name.append(i[0])
        fail_num = fail_num + fail_count
    # 返回失败用例总数和存在错误的表名
    return fail_num, tb_name
