import pymysql

# 连接数据库
config = {
    'host': '192.168.3.19',
    'port': 3306,
    'user': 'root',
    'passwd': 'hongwei',
    'charset': 'utf8mb4',
    'db': 'test',
    'cursorclass': pymysql.cursors.DictCursor
}
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()

try:
    # 创建数据库
    # DB_NAME = 'test'
    # cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
    # cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % DB_NAME)
    # conn.select_db(DB_NAME)

    # 创建表
    # TABLE_NAME = 'user'
    # cursor.execute(
    #     'CREATE TABLE %s(id int primary key,name varchar(30))' % TABLE_NAME)

    # 批量插入纪录
    values = []
    for i in range(2):
        values.append((i, 'luoyc' + str(i)))
    cursor.executemany('INSERT INTO user values(%s,%s)', values)
    print(values)

    # 查询数据条目
    # TABLE_NAME = 'user'
    # FIELD_NAME = 'ID'
    # STR_NAME = '1'
    # count = cursor.execute('SELECT * FROM %s WHERE %s = %s' % (TABLE_NAME, FIELD_NAME, STR_NAME))
    # # 显示所有结果
    # cds = cursor.fetchall()
    # print('total records:', cursor.rowcount)
    # print(cds)

    # 获取表名信息
    # desc = cursor.description
    # print("%s %s" % (desc[0][0], desc[1][0]))

except Exception:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
