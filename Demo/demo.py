import hashlib

m2 = hashlib.md5()
m2.update("abc123")
print(m2.hexdigest())
