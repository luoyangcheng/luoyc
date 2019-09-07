import flask,json

server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动

@server.route('/index',methods=['get', 'post'])#第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get

def index():
    username=flask.request.values.get('username')
    res={'msg':username,'msg_code':200}
    return json.dumps(res,ensure_ascii=False)

server.run(port=7777,debug=True,host='0.0.0.0')