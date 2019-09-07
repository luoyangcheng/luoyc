# encoding=utf-8
import requests
import time

# 广州-客栈
cookies = {"mz_UCLBRTUID": "9cecb07d-4eb0-4551-a7d9-8f69fafcedda",
           "mz_UCLBRTUSSID": "RH6AvvpgYSgHUMvmkyMzsx96IHq6MePqqq%2BanvOr85aT%2F5lAYU3cVqjvKUg2295a4lJs1DkGYYjBzUWmg%2B6HotZnk6CcZ9vwpH9lf7ufnkUXa5tJdCdMfTqaUu0EWfzV8WcogdAertm0i%2BjMw0Ow7vJEG1Fzeq4%2BLduo3SYF5Y5EIK%2BGXstn3n2MRJemJjXkrIQgUnSoOp0Re40DYNQlv%2Bzc6WSxJ%2BbNDJuJJwqOVwyOqT5tqb6TiHTYd1dt08tlEdpWbkw2Ctu5gkhBbmU7PBxbY7KmoDemEzfXw1VKN4OiMZMdddq78%2FeHgbGXW56vZkWirXRXiekpfgMMRy0g%3D%3D",
           "mz_UCLBRTUSSPS": "971c9a641cf2b71d805bd50833405f11130eef45dec9e7950843fe2009fb0aa53a20d7c004f4de05242c93cd52f121c20705f6fe00eaa2d9966f21af0777386f",
           "mz_UCLBRTPSTM": "1526971668",
           "mz_think_language": "zh_cn",
           "mz_room_view_style": "1",
           "master_session_id": "6munomg819qi3lds2niu4qj142",
           "qrm_community_identity": "x7zjDYALp4AlbMgE",
           "monitor_count": "70",
           "qrm_think_language": "zh_cn"}
host = "http://115.29.142.212:8020"
url = "/Home/Room/addRooms"
link = host + url
for i in range(250):
    data = {"build": "973",
            "floor": "4274",
            "rooms[0][name]": '6'+str(i),
            "rooms[0][num]": str(i),
            "rooms[0][no]": str(i),
            "rooms[0][locktype]": "1",
            "rooms[0][layout]": '{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
            }
    print(data)
    time.sleep(0.5)
    req = requests.post(link, cookies=cookies, data=data)
    print(req.text)
