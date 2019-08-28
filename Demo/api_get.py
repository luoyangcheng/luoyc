import pymysql
from wsgiref.simple_server import make_server


def hello(environ, start_response):
    co = pymysql.connect('192.168.3.19', 'root', 'hongwei', "luoyc")
    cursor = co.cursor()
    sql2 = 'select * from user'
    cursor.execute(sql2)
    re = cursor.fetchall()
    co.commit()
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [re]


httpd = make_server('192.168.3.188', 5088, hello)
print('Serving HTTP on port 5088...')
# 开始监听HTTP请求:
httpd.serve_forever()
