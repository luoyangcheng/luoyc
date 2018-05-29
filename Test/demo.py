import requests


class login:
    def ll(communityId, id, token):
        data = {'communityId': communityId,
                'id': id,
                'token': token}

        login_url = "http://192.168.3.19:6112/Mobile/Room/item"

        session = requests.Session()
        for i in range(10):
            resp = session.post(login_url, data)
            print(resp.content.decode('utf-8'))


if __name__ == '__main__':
    login.ll('537', '2402',
             'V2Kog/Nd3SGve9l1Ds8jf2I6R492mVmIG9KG1arGyO7wyIq7rRjACV8HtzmTd0KU20XiDGac1rBVZrP8ut6SBzT+WhFmCbEJCWww8qdsEEX2IZ0kZ0NART5bZY4dmRyXMGC6gcr/YodbePrcPP98TKrOO0NY+XIM3PvojESD5fQ56G5Y5EGoevZCExeOaYbSR7VHxVVvdxbCmKJGZkw4y2ccR+nvBPZC5ge8GT5FcfNpegel9sw9/kU6Tam6GqfpYDSwZCA8vabGzpKmnUXYlHdpu1qss4pXkzl0KH7dcpAhJFVxtlhOdPqtxegTV3ZfOa9o+Q0WOTxnstjoFRbnCw==')
