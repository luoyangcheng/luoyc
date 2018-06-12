import requests
import json
import urllib


def getBshijianImag(path, goodsid):
    try:
        url = 'https://app.bicijian.com/index.php?act=goods&op=goods_detail&goods_id=' + str(goodsid) + '&key=&dis_id='
        str(url)
        imgs = requests.get(url)
        f = json.loads(imgs.text)
        img_urls = []
        for i in range(len(f["datas"]["image_list"])):
            datas = (f["datas"]["image_list"][i]["_big"])
            img_urls.append(datas)
        m = 1
        for img_url in img_urls:
            print(str(goodsid) + str(m) + '.jpg')
            urllib.request.urlretrieve(img_url, path + str(goodsid) + '_' + str(m) + '.jpg')
            m = m + 1
        print('商品ID为：'+str(goodsid)+'的图片下载完成!')
    except:
        print("该商品ID不存在或者已被删除")


if __name__ == '__main__':
    for goodsid in range(430195, 430199):
        getBshijianImag('F:/A/', goodsid)
