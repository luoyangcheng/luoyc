import requests
from lxml import etree


def get_usefulip():
    url='https://www.xicidaili.com/wn/'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
    response=requests.get(url=url,headers=headers)
    HTML=etree.HTML(response.text)
    ip_list=HTML.xpath('//tr[@class="odd"]/td[2]/text()')   # IP
    port_list=HTML.xpath('//tr[@class="odd"]/td[3]/text()')  # 端口号

    ip_useful=[]
    for i in range(len(port_list)):
        ip_list[i]+=':{}'.format(port_list[i])
        proxies={'https':ip_list[i]}
        print(ip_list[i],end=' ')
        try:
            response_1=requests.get(url='https://www.baidu.com/',proxies=proxies,timeout=6)
            # timeout 超时设置
            print(response_1.status_code)
            if response_1.status_code==200:
                ip_useful.append(ip_list[i])
        except:
            print('无用IP！')
    return ip_useful


with open(file='./ip.txt',mode='w',encoding='utf-8') as f:
    for i in get_usefulip():
        f.write(i+'\n')
