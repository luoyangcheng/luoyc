import requests, time, calendar
import hashlib

api_timestamp = str(calendar.timegm(time.gmtime()) * 1000)
print(api_timestamp)