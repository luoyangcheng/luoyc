import requests
import json
import urllib.request
import os


def mkdirfile(file_path):
    folder = os.path.exists(file_path)
    if not folder:
        os.makedirs(file_path)
        print("File created successfully")
    else:
        print("File already exists")


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
        print('The download is complete，goods_id：【' + str(goods_id) + '】')
    except:
        print('The commodity department exists or has been deleted, goods_id：【' + str(goods_id) + '】')


if __name__ == '__main__':
    mk_file_path = 'C:/BCJ_image/'
    mkdirfile(mk_file_path)
    for goods_id in range(430187, 430188):
        getBicijianImag(mk_file_path, goods_id)
