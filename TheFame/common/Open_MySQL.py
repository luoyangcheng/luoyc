import pymysql


class DATA(object):
    try:

        def __init__(self):
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
            self.conn = pymysql.connect(**config)
            self.conn.autocommit(1)
            self.cursor = self.conn.cursor()

        # 创建数据库
        def CREATE_DB(self):
            DB_NAME = 'test'
            self.cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
            self.cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % DB_NAME)
            self.conn.select_db(DB_NAME)
            # 关闭游标连接
            self.cursor.close()
            # 关闭数据库连接
            self.conn.close()

        # 创建表
        def CREATE_TABLE(self):
            TABLE_NAME = 'user'
            self.cursor.execute(
                'CREATE TABLE %s(id int primary key,name varchar(30))' %
                TABLE_NAME)
            self.cursor.close()
            self.conn.close()

        # 批量插入纪录
        def ADD_ADTA(self):
            values = []
            for i in range(3, 4):
                values.append((i, 'luoyc' + str(i)))
            self.cursor.executemany('INSERT INTO user values(%s,%s)', values)
            self.cursor.close()
            self.conn.close()
            print(values)

        # 查询数据条目
        def SELECT(self):
            TABLE_NAME = 'user'
            FIELD_NAME = 'ID'
            STR_NAME = '1'
            self.count = self.cursor.execute(
                'SELECT * FROM %s WHERE %s = %s' % (TABLE_NAME, FIELD_NAME,
                                                    STR_NAME))
            # 显示所有结果
            cds = self.cursor.fetchall()
            self.cursor.close()
            self.conn.close()
            print('total records:', self.cursor.rowcount)
            print(cds)

        # 修改数据
        def UPDATE(self):
            TABLE_NAME = 'user'
            FIELD_NAME = 'ID'
            STR_NAME = '1'
            self.cursor.execute('UPDATE %s SET %s = "1" WHERE %s = 1' %
                                (TABLE_NAME, STR_NAME, FIELD_NAME))
            self.cursor.close()
            self.conn.close()

        # 删除数据
        def DELETE(self):
            TABLE_NAME = 'user'
            FIELD_NAME = 'ID'
            STR_NAME = '1'
            self.cursor.execute('DELETE FROM %s WHERE %s = %s' %
                                (TABLE_NAME, FIELD_NAME, STR_NAME))
            self.cursor.close()
            self.conn.close()

    except Exception as e:
        print(e)