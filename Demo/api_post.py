import json
import pymysql
from wsgiref.simple_server import make_server


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response("200 OK", [("Content-Type", "application/json")])
    # environ是当前请求的所有数据，包括Header和URL，body

    request_body = environ["wsgi.input"].read(
        int(environ.get("CONTENT_LENGTH", 0)))
    request_body = json.loads(request_body.decode('utf-8'))
    id = request_body["id"]

    # input your method here
    # for instance:
    # 增删改查
    co = pymysql.connect('192.168.3.19', 'root', 'hongwei', "luoyc")
    cursor = co.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id,name,password,Email from user where id =%s',
                   (id))
    re = cursor.fetchall()
    co.commit()

    dic = {'date': re}
    dit = "没有此id"

    if id == "5":
        return [json.dumps(dit).encode('utf8')]
    else:
        return [json.dumps(dic).encode('utf8')]


if __name__ == "__main__":
    port = 6088
    httpd = make_server("192.168.3.188", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
