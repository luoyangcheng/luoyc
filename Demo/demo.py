import requests
import json
import urllib


def getSogouImag(path):

    imgs = requests.get('https://app.bicijian.com/index.php?act=goods&op=goods_detail&goods_id=430198&key=&dis_id=')
    f = json.loads(imgs.text)
    vids = []
    for i in range(len(f["datas"]["image_list"])):
        vid = (f["datas"]["image_list"][i]["_small"])
        vids.append(vid)
    print(vids)
    m = 0
    for img_url in vids:
        print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
        urllib.request.urlretrieve(img_url, path + str(m) + '.jpg')
        m = m + 1
    print('Download complete!')


if __name__ == '__main__':
    getSogouImag('F:/A/')
