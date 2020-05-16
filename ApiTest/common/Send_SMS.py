from twilio.rest import Client


def SendSMS():
    sid = 'ACce24d396e0802184da660c363223e658'
    token = 'f91a0bc13e71427780d016f794535917'
    content = '测试完成！测试报告：http://94.191.124.146/TheFame/report/Meizhu.html'
    try:
        client = Client(sid, token)
        Message = client.messages.create(to='+8618802094078', from_='+19282914558', body=content)
    except Exception as e:
        print('短信发送失败！', e)
    else:
        print('短信发送成功！', Message.sid)
