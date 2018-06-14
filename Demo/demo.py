all = []
for i in range(2):
    a = []
    for j in range(5):
        a.append(j)
    if a not in all:
        all.append(a)
    else:
        print("已存在")
    print(a)
print(all)
