import time
import os
from PIL import ImageGrab


def mkdirfile(file_path):
    folder = os.path.exists(file_path)
    if not folder:
        os.makedirs(file_path)
        print("File created successfully")
    else:
        print("File already exists")


def picture():
    nowDate = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    mkdirfile('../TheFame/report/%s/' % (nowDate))
    nowTime = int(time.time())
    im = ImageGrab.grab()
    im.save('../TheFame/report/%s/%s.jpg' % (nowDate, nowTime))
