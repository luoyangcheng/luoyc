import json

id = 'XXXX'
data = [{"body": {"cityId": "440100", "orgNo": "66666662"}, "header": {"requestId": "472158bd6c5b8eb7dfe88ed94ee2d51c", "timeStamp": 1630293075151, "applicationId": "b2c-mobile", "ip": "0.0.0.0", "version": "TRIAL", "tokenId": "#ywzt#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2Mjk4NzEyNjUsImV4cCI6MTYyOTk1NzY2NSwiaXNzIjoiTWVtYmVyIiwic3ViIjoiNTEzMzAzMjAifQ.TVFvoZGC4DE0UTGLuipUTqeoBj0inB-shzEhazW_D0sTnnHwf_GMPDEcecuM05-bNVYg2ryg_UY0mLuYhMwtOQ"}}]

if 'header' in data[0]:
   data[0]["header"]["tokenId"]=id
   print(data)