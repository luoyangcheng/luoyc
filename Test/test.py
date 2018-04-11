from datetime import datetime,timedelta
import hashlib
import hmac
import itertools
from PIL import Image
import requests
from tkinter import *
import tkinter.messagebox as messagebox
import socket
import threading
import pymysql

# now = datetime.now()
# print(now)
# print(now.timestamp())
# print(datetime.utcfromtimestamp(now.timestamp()))
#
# str=datetime.strptime('2018-04-09 10:10:10','%Y-%m-%d %H:%M:%S')
# print(str)
#
# print(now.strftime('%a, %b %d %H:%M'))
#
# a = '12:13:50'
# b = '12:28:21'
# time_a = datetime.strptime(a,'%H:%M:%S')
# time_b = datetime.strptime(b,'%H:%M:%S')
# print(time_b - time_a)
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib??'.encode('utf-8'))
# print(md5.hexdigest())
#
# message=b'6534563563563563'
# key=b'asdddd'
# h=hmac.new(key,message,digestmod='MD5')
# print(h.hexdigest())

# image = Image.open('F:/aa.jpg')
# w ,h = image.size
# print('Original image size: %sx%s' % (w, h))
# image.thumbnail((w//2,h//2))
# image.save('F:/aa1.jpg','jpeg')

# r = requests.get('https://www.douban.com/')
# print(r.text)
# print(r.status_code)
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     data = sock.recv(1024)
#     if data.decode('utf-8') == 'exit':
#         sock.close()
#     sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     print('Connection from %s:%s closed.' % addr)
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 5555))
# s.listen(5)
# print('Waiting for connection...')
# while True:
#     sock, addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

# co = pymysql.connect('192.168.3.19', 'root', 'hongwei',"luoyc")
# cursor = co.cursor()
# # DB_NAME = 'luoyc'
# # cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
# # cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
# # co.select_db(DB_NAME)
# # TABLE_NAME = 'user'
# # cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' %TABLE_NAME)
# n ="kk"
# sql = 'INSERT INTO user (id, name) VALUES (%s,%s)',(4,n)
# sql2 = 'select * from user'
# # cursor.execute('INSERT INTO user (id, name) VALUES (%s,%s)',(4,n))
# cursor.execute(sql2)
# re = cursor.fetchall()
# co.commit()
# print(re)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()