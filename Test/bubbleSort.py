#冒泡排序
def bubbleSort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


nums = [5, 2, 45, 6, 8, 3, 1]

print(bubbleSort(nums))
