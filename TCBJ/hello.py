import requests, time, calendar
import hashlib

header = {"associatedId": "178908226"}
api_appKey = 'lxb7f4e2c0d115372d'
api_timestamp = str(calendar.timegm(time.gmtime()) * 1000)
api_version = '1.0'
appSecret = 'cfdc9af6fe75e11e7008c954dfab681c1a95b506'
sss = [appSecret, api_appKey, api_timestamp, api_version]
adc = ''.join(sorted(sss))


def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf8"))
    return m.hexdigest()


a = md5(adc)
b = a.upper()

api_sign = b
url = 'http://api.leshiguang.com/api/family/v1.0/counselorModification/queryCustomerBindInfo?api_appKey=' + api_appKey + '&api_timestamp=' + api_timestamp + '&api_sign=' + api_sign + '&api_version=1.0&associatedId=178908226'
res = requests.get(url)
r = res.content.decode('utf-8')
print(api_timestamp)
print(r)