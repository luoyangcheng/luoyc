# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
import re
import time

# 锁掌柜
qrm_client = 'http://115.29.142.212:8020'

# 锁掌柜bpass
qrm_bpass = "http://115.29.142.212:8021"
qrm_bpass_login_url = qrm_bpass + '/Bpass/Public/doLogin'

# 美住
mz_client = 'http://115.29.142.212:8010'

#美住bpass
mz_bpass = 'http://115.29.142.212:8012'

# 锁掌柜账号
qrm_bpass_data = {
    "username": "changlian",
    "password": "49dec5fb8af4eeef7c95e7f5c66c8ae6"
}
# 锁掌柜账号
qrm_client_data = {
    "mobile": "13326528030",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
# 集群信息
qrm_community_data = {
    "universalTime": "5",
    "desc": "333",
    "type": "1",
    "addr": "11",
    "cont": "联系人",
    "phone": '13480251015',
    "areaCode": "1"
}
# 美住客栈信息
mz_hotel_data = {
    'city': '320700',
    'district': '320704',
    'universalTime': '5'
}

# 美住登陆客栈信息：
mz_login_data = {
    'mobile': '13326528030',
    'password': '111111b',
    'areaCode': '86',
}


def mz_add_hotel(mz_client_s):
    mz_client_s.post(mz_client + '/Home/Hotel/addHotel', data=mz_hotel_data)


def mz_login_bpass(b):
    login_html = b.get(mz_bpass + '/index.php/Home/Public/login.html')
    soup = BeautifulSoup(login_html.text, "html.parser")
    vcode_src = mz_bpass + soup.find('img', id='imgcode')['src']
    while True:
        # 获取验证码
        vcode_img = b.get(vcode_src)
        with open('mz_vcode.png', 'wb') as fb:
            fb.write(vcode_img.content)
        vcode = input("输入验证码")
        mz_bpass_login = {
            'username': 'changlian',
            'password': 'bbc69d27003568a7a94626ce4337bc9d',
            'vcode': vcode,
        }
        info = b.post(mz_bpass + '/Home/Public/checkLogin', data=mz_bpass_login)
        if info.status_code == 200:
            break
    return b

# 通过客栈审核
def mz_bpass_pass_hotel(b, h_name):
    info = b.get(mz_bpass + "/index.php/Home/HotelApply/index.html")
    soup = BeautifulSoup(info.text, 'html.parser')

    td_list = soup.find('td', text=h_name).parent.find_all('td')
    h_info = json.loads(td_list[-1].button['data-json'], encoding='utf-8')
    mz_bpass_apply_data = {
        'universalTime': h_info['universaltime_id'],
        'areacode': h_info['areacode'],
        'mobile': h_info['mobile'],
        'city': h_info['city_id'],
        'district': h_info['district_id'],
        'hotel': h_info['hotelname'],
        'id': h_info['id'],
        'username': h_info['username'],
        'kaitongDate': '1',
    }
    b.post(mz_bpass + '/Home/HotelApply/handle', data=mz_bpass_apply_data)

# 美住添加房间
def mz_add_room(s):
    info = s.get(mz_client + '/Home/RoomPage/index.html')
    soup = BeautifulSoup(info.text, 'html.parser')
    # 找到最后一个客栈的hotel_id
    hotel_id = soup.find('tbody', id='roomTypeHotelList').find_all('tr')[-1]['data-id']
    mz_room_data = {
        'room': '1,2,3,4,5',
        'hotel': hotel_id,
        'name': '单人间',
        'price': '100'
    }
    s.post(mz_client+'/Home/Room/addRoom',data=mz_room_data)
    params = {
        'hotel':hotel_id
    }

def md5(str):
    m = hashlib.md5(str.encode("utf-8"))
    return m.hexdigest()


# 抓取页面的hash值
def get_hash(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    # print(soup.prettify())
    info = soup.find_all("div", class_="card")
    for i in info:
        hash = i['data-hash']
    return hash


# 处理从网页得到的hash值
def handle_hash(data, hash):
    # hash 规则为 MD5（密码+md5(mobile)）+$("#login-container").data("hash"))
    mobile_pwd = md5(data['password'] + md5(data['mobile']))
    mobile_pwd_hash = mobile_pwd + hash
    data['hash'] = md5(mobile_pwd_hash)

# 切换集群
def change_commuity(s):
    info = s.get(qrm_client + '/userCenter.html')
    main_info = BeautifulSoup(info.text, "html.parser")
    com_list = main_info.find('ul', id='communitySwitch')
    no_a = com_list.find('ul', class_='dropdown-menu')
    a_list = no_a.find_all('a')
    group_no = 0
    for i in a_list:
        if qrm_community_data['cname'] in i.string:
            group_no = i['data-value']
    # 获取no，发送请求
    group_data = {
        'no': group_no,
        'return': '/userCenter.html'
    }
    s.get(qrm_client + '/Home/CommunityPage/entry.html', params=group_data)
    s.get(qrm_client + '/userCenter.html')
    return s


# 申请审核
def qrm_apply_verity(s):
    img_url = up_image(s)
    print(qrm_client + img_url)
    apply_data = {
        "isforeign": "0",
        "companyname": "畅联",
        "address": "guangdong",
        "representative": "555",
        "telephone": "13480251015",
        "fax": "",
        "business": "444",
        "bpath": img_url,
        "areaCode": "86"
    }
    response = s.post(qrm_client + '/Home/CommunityCenter/postAuthenticationCompany', data=apply_data).json()


# 上传图片
def up_image(s):
    img_file = {
        'config': (None, 'comVerify'),
        'file': open(r'./verify.png', 'rb')}
    response = s.post(qrm_client + '/Home/File/upload', files=img_file).json()
    file_url = response['data']['filename']
    return file_url


# 同步美住客栈
def syn_community(s):
    s = syn_login_meizhu(s)
    resp_data = s.post(qrm_client + '/Home/Sync/getHotel').json()
    com_data = resp_data['data'][-1]
    # 此时得到的com_data 中的communityid是为0
    params = {
        "hotelid": com_data["hotelentity_id"],
        "hotelname": com_data["name"],
        "communityid": com_data["communityid"],
        "universaltime_id": com_data["universaltime_id"],
        "communityname": com_data["name"]
    }
    data = {
        "hotels": '[' + json.dumps(params, ensure_ascii=False) + ']'
    }
    syn_url = qrm_client + '/Home/Sync/syncCommunity'
    s.post(syn_url, data=data)
    # 重复请求getHotel 得到community_no
    resp_data = s.post(qrm_client + '/Home/Sync/getHotel').json()
    com_data = resp_data['data'][-1]
    com_data['communityid'] = com_data['communityid']

    # 同步房间
    hotel_data = {
        'hotelId': com_data["hotelentity_id"],
        'communityId': com_data["communityid"],
    }
    print(hotel_data)
    res = s.post(qrm_client + '/Home/Sync/getRoom', data=hotel_data).json()
    print(res)
    room_dict = {}
    room_list = []
    room_str = ''
    for room in res['data'][0]['room']:
        room_dict['id'] = room['id']
        room_dict['name'] = room['name']
        room_list.append(room_dict)
        room_str = room_str + json.dumps(room_dict) + ','
    add_room_data = {
        'hotelId': com_data["hotelentity_id"],
        'communityId': com_data["communityid"],
        'builderName': '楼栋1',
        'builderNum': '1',
        'floorName': '楼层1',
        'floorNum': '1',
        'roomsAdd': '[' + room_str[0:room_str.__len__() - 1] + ']',
    }
    print(add_room_data)
    s.post(qrm_client + '/Home/Sync/syncRoomAdd', data=add_room_data)


#修改锁的类型为二维码
def update_room_type(s):
    req_url = qrm_client + '/Home/Room/saveRoom'
    room_data = get_all_room_info(s)
    for i in range(room_data.__len__()):
        for single_room in room_data:
            single_room['locktype'] = '1'
            s.post(req_url, data=single_room)

#得到锁掌柜所有的房间信息
def get_all_room_info(s):
    # 得到每个房间页面的请求链接
    req_index_url = qrm_client + '/room.html'
    room_html = s.get(req_index_url)
    soup = BeautifulSoup(room_html.text, "html.parser")
    div_tag = soup.find('div', id='doc-center-page')
    # print(table.tbody.tr.next_sibling.next_sibling)
    page_url = div_tag.find_all('a')
    page_url = page_url[:-page_url.__len__():-1]
    page_url_list = []
    for i in page_url:
        page_url_list.append(i['href'])
    page_url_list.append('room_1.html')
    list_data = []
    for url in page_url_list:
        # 房间id:'room' 房间名：'name'房间号:'no' 锁编号：'num' 锁类型'locktype'
        req_url = qrm_client + '/' + url
        data = s.get(req_url)
        soup = BeautifulSoup(data.text, "html.parser")
        table_soup = soup.find('table', id='roomTable')
        # 玫瑰花客栈-测试
        tr_list = table_soup.tbody.find_all('tr')
        # 计算tr的数量，得到有多少个房间
        num = 0
        for i in tr_list:
            num += 1
        tr_soup = table_soup.tbody.tr
        td_soup = tr_soup.td
        count = 0
        while True:
            data = {}
            for i in range(16):
                td_soup = td_soup.next_sibling
            data_room = {}
            data_room['room'] = td_soup['data-value']
            data_room['name'] = td_soup['data-name']
            data_room['no'] = td_soup['data-no']
            data_room['num'] = td_soup['data-num']
            data_room['locktype'] = td_soup['data-locktype']
            list_data.append(data_room)
            count += 1
            if count == num:
                break
            tr_soup = tr_soup.next_sibling
            td_soup = tr_soup.td
    return list_data

# 在锁掌柜登陆美住账号
def syn_login_meizhu(s):
    sync_switch_url = qrm_client + '/Home/Sync/switchAccount'
    data = {
        'meizhu': '13326528030',
        'password': '111111b',
        'areaCode': '86'
    }
    s.post(sync_switch_url, data=data)
    return s


# 锁掌柜bpass
def qrm_bpass_login(s):
    html_doc = s.get(qrm_bpass+'/Bpass/Public/login.html').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    img = soup.find("img", {"id": "imgcode"})
    print(img)
    img_path = qrm_bpass + img["src"]
    # req.get()得到一个response对象，对象存服务器返回的信息，
    # 返回的页面会存在.content和.text对象。
    # .content返回的是字节码
    # .text存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
    while True:
        image = s.get(img_path, stream=True).content
        with open('./qrm_vcode.jpg', 'wb') as fd:
            fd.write(image)
        vcode = input("请输入验证码")
        qrm_bpass_data['vcode'] = vcode
        r = s.post(qrm_bpass_login_url, data=qrm_bpass_data).json()
        if r['status'] == 200:
            break


#锁掌柜通过认证
def pass_group_verity(req, qrm_community_data):
            query_verify_url = qrm_bpass + '/Bpass/ComAuthority/company.html'
            group_data = {
                'type': '',
                'status': '',
                'name': qrm_community_data['cname'],
                'no': ''
            }
            print(group_data)
            query_group = req.get(query_verify_url, params=group_data)
            soup = BeautifulSoup(query_group.text, 'html.parser')
            s_table = soup.find('table', id='questionTalbe')
            a_list = s_table.find_all('a')
            a_href = a_list[-1]['href']
            reObj1 = re.compile('[0-9]+')
            id = reObj1.findall(a_href)[0]
            page_id = reObj1.findall(a_href)[1]
            # 通过审核
            verify_page_url = qrm_bpass + '/Bpass/ComAuthority/companyStatus/id/' + id + '/userloginID/' + page_id + '.html'
            verify_data = {
                "id": (None, id),
                "status": (None, "3"),
                "agencyId": (None, "1"),
                "representative": (None, "33323"),
                "hotelSign": (None, "00000"),
                "brandTypeId": (None, "1"),
                "typeSignId": (None, "1"),
                "authorityNote": (None, "22244"),
            }
            req.post(verify_page_url, files=verify_data)

# 新建美住客栈，通过审核，新建房间，在锁掌柜同步集群，同步房间，修改房间为二维码房间，
if __name__ == "__main__":
    # 1、美住：登陆美住客栈
    h_name = input('输入客栈名称')
    # 河源客栈-有为测试
    mz_hotel_data['hotel'] = h_name.strip()
    mz_client_s = requests.session()
    mz_client_s.get(mz_client + '/Home/BookPage/index.html')
    mz_client_s.post( mz_client + '/Home/Public/login', data=mz_login_data)
    #
    #  2、美住：创建美住客栈
    mz_add_hotel(mz_client_s)
    #
    #  3、登陆bpass
    mz_bpass_s = requests.session()
    mz_bpass_s = mz_login_bpass(mz_bpass_s)
    #
    # 4、美住客栈通过审核
    mz_bpass_pass_hotel(mz_bpass_s, h_name)
    #
    # 5、美住新建房间
    mz_add_room(mz_client_s)


    # 6、登陆锁掌柜
    qrm_client_s = requests.session()
    qrm_community_data['cname'] = h_name
    html_doc = qrm_client_s.get(qrm_client + '/login.html').text
    hash = get_hash(html_doc)
    handle_hash(qrm_client_data, hash)
    qrm_client_s.post(qrm_client + '/Home/Public/login', data=qrm_client_data)

    # 7、进入锁掌柜同步中心，登陆美住账号,同步集群,同步房间
    syn_community(qrm_client_s)

    # 8、切换到同步集群,修改房间类型为二维码房间
    qrm_client_s = change_commuity(qrm_client_s)
    update_room_type(qrm_client_s)

    #9、锁掌柜申请认证
    qrm_apply_verity(qrm_client_s)

    #10 登陆锁掌柜bpass，通过认证
    qrm_bpass_s = requests.session()
    qrm_bpass_login(qrm_bpass_s)
    pass_group_verity(qrm_bpass_s, qrm_community_data)




