import collections


def func(arr):
    arr = collections.Counter(arr).most_common()
    tempArr = []
    itemMax = arr[0][1]
    for item in arr:
        if item[1] > itemMax:
            itemMax = item[1]
    for item in arr:
        if item[1] == itemMax:
            tempArr.append(item[0])
    return tempArr


arr = []
arrRed = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
arrBlack = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red = 0
black = 0
while True:
    n = int(input("n = "))
    if n < 0 or n > 36:
        exit(0)
    if len(arr) > 12:
        arr.pop(0)
    arr.append(n)

    print(func(arr))

    for i in range(0, 37):
        if not arr.__contains__(i):
            print(i, end=" ")
    print("")

    if arrRed.__contains__(n):
        red += 1
    elif arrBlack.__contains__(n):
        black += 1
    print(red, black, sep=" ")
