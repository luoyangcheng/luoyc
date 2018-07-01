mobile = 18802094078
password = 'qq111111'

i = 0
while i < 5:
    m = input("请输入手机号：")
    try:
        m = int(m)
    except Exception as e:
        print('手机号格式错误', e)
    if m == mobile:
        j = 0
        while j < 5:
            p = input('请输入密码：')
            if p == password:
                print('登陆成功')
            elif j < 4:
                j = j + 1
            else:
                print('密码错误超过5次，请稍后再试')
                break
    else:
        print('账号不存在')
        i = i + 1
