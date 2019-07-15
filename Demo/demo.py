# 递归函数，比如可以用来计算:1*2*3...*n = ?
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3] # 从第一个开始，取前面三个值
L[-1] # 取倒数第一个值