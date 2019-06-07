import urllib
from PIL import Image
import pytesseract


def img():
    url = 'http://cz.uclbrt.com/Wap/Public/createpic'
    x = 0
    path = 'D:/demo/'
    img_URL = url
    print(img_URL)
    urllib.request.urlretrieve(img_URL, path + '%s.png' % x)
    x = x + 1
    print('正在下载：' + img_URL)


def binarization(img_path, threshold):
    image = Image.open(img_path)
    image = image.convert('L')  # 图片灰度处理
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    # image.show()
    return image


def identify(img_path, threshold):
    image = binarization(img_path, threshold)
    vcode = pytesseract.image_to_string(image)
    print('识别为：' + vcode)


if __name__ == '__main__':
    identify('D:/demo/3.png', 130)
