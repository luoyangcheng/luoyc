import requests
import json
import urllib
import os


def mkdirfile(file_path):
    folder = os.path.exists(file_path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(file_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("创建文件成功")
    else:
        print("文件已存在")


def getBicijianImag(path, goods_id):
    try:
        url = 'https://app.bicijian.com/index.php?act=goods&op=goods_detail&goods_id=' + str(goods_id) + '&key=&dis_id='
        str(url)
        img_s = requests.get(url)
        f = json.loads(img_s.text)
        img_urls = []
        for i in range(len(f["datas"]["image_list"])):
            data_s = (f["datas"]["image_list"][i]["_big"])
            img_urls.append(data_s)
        m = 1
        for img_url in img_urls:
            print(str(goods_id) + str(m) + '.jpg')
            urllib.request.urlretrieve(img_url, path + str(goods_id) + '_' + str(m) + '.jpg')
            m = m + 1
        print('商品ID为：' + str(goods_id) + '的图片下载完成!')
    except:
        print("该商品ID不存在或者已被删除")


if __name__ == '__main__':
    file = 'C:/xxoo/'
    mkdirfile(file)
    for goods_id in range(430195, 430199):
        getBicijianImag(file, goods_id)
