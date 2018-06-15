all = []
for i in range(2):
    a = []
    for j in range(5):
        a.append(j)
    if a not in all:
        all.append(a)
        print(a)
    else:
        print("已存在")
print(all)

c = [[1,2],[3,4]]
d = [3,45]
e = c[0]
if d not in c:
    print(0)
else:
    print(1)
print(e)