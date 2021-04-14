import json

class LoginHandler(RequestHandler):
    def post(self):
        req_data = json.loads(self.request.body)

        js_code = req_data.get('js_code')

        # 这里是换取用户的信息
        user_info = get_user_info(js_code=js_code)

        openid = user_info['openid']
        session_key = user_info['session_key']
        user_uuid = str(uuid.uuid4())  # 暴露给小程序端的用户标示

        # 用来维护用户的登录态
        User.save_user_session(user_uuid=user_uuid, openid=openid, session_key=session_key)
        # 微信小程序不能设置cookie，把用户信息存在了 headers 中
        self.set_header('Authorization', user_uuid)

        # 存储用户信息
        User.save_user_info(open_id=openid)

        self.set_status(204)