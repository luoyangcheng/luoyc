import re

test = 'lyc163069@163.com'
if re.match(r'^[0-9a-zA-z]+\@[0-9a-zA-z]+\.[a-zA-z]+$', test):
    print('ok')
else:
    print('failed')


print('a b   c'.split(' '))
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
