import requests
import json
import urllib.request
import os
import time


def mkdirfile(file_path, goods_id, code, img_urls, all_img):
    if code == 200 and img_urls not in all_img:
        folder = os.path.exists(file_path)
        if not folder:
            os.makedirs(file_path)
            print("File created successfully")
        else:
            print("File already exists")
    else:
        print('The commodity department exists or has been deleted, goods_id：【' + str(goods_id) + '】')


def getBicijianImag(path, goods_id, img_urls, all_img):
    if img_urls not in all_img:
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
    else:
        print("Data already exists")


if __name__ == '__main__':

    i = 0
    while (i < 10):
        star1 = input("请输入开始商品ID（输完按回车）:")
        star = int(star1)
        end1 = input("请输入结束商品ID（输完按回车）:")
        end = int(end1)
        if star < end:
            all_img = []
            for goods_id in range(star, end):
                url = 'https://app.bicijian.com/index.php?act=goods&op=goods_detail&goods_id=' + str(
                    goods_id) + '&key=&dis_id='
                img_s = requests.get(url)
                f = json.loads(img_s.text)
                code = f["code"]
                if code == 200:
                    name = f["datas"]["goods_info"]["goods_name"]
                    mk_file_path = 'C:/BCJ_image/' + str(name) + '/'
                    img_urls = []
                    for i in range(len(f["datas"]["image_list"])):
                        data_s = (f["datas"]["image_list"][i]["_big"])
                        img_urls.append(data_s)
                    mkdirfile(mk_file_path, goods_id, code, img_urls, all_img)
                    getBicijianImag(mk_file_path, goods_id, img_urls, all_img)
                    if img_urls not in all_img:
                        all_img.append(img_urls)
                    else:
                        print('Data already exists')
                else:
                    print('The commodity department exists or has been deleted, goods_id：【' + str(goods_id) + '】')
            wait = input("请按回车键结束程序")
            break
        else:
            print("开始商品ID不能大于结束商品ID，请重新输入")
            i = i + 1
