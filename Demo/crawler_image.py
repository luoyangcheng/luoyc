import requests
import json
import urllib.request
import os
import time


def mkdirfile(file_path, goods_id, code):
    if code == 200:
        folder = os.path.exists(file_path)
        if not folder:
            os.makedirs(file_path)
            print("File created successfully")
        else:
            print("File already exists")
    else:
        print('The commodity department exists or has been deleted, goods_id：【' + str(goods_id) + '】')

def getBicijianImag(path, goods_id,img_urls):
    try:
        m = 1
        for img_url in img_urls:
            print(str(goods_id) + str(m) + '.jpg')
            urllib.request.urlretrieve(img_url, path + str(goods_id) + '_' + str(m) + '.jpg')
            time.sleep(1)
            m = m + 1
        print('The download is complete，goods_id：【' + str(goods_id) + '】')
    except:
        print('The commodity department exists or has been deleted, goods_id：【' + str(goods_id) + '】')


if __name__ == '__main__':
    for goods_id in range(430188, 430198):
        url = 'https://app.bicijian.com/index.php?act=goods&op=goods_detail&goods_id=' + str(goods_id) + '&key=&dis_id='
        img_s = requests.get(url)
        f = json.loads(img_s.text)
        code = f["code"]
        name = f["datas"]["goods_info"]["goods_name"]
        mk_file_path = 'C:/BCJ_image/' + str(name) + '/'
        img_urls = []
        for i in range(len(f["datas"]["image_list"])):
            data_s = (f["datas"]["image_list"][i]["_big"])
            img_urls.append(data_s)
        mkdirfile(mk_file_path, goods_id,code)
        getBicijianImag(mk_file_path, goods_id,img_urls)
