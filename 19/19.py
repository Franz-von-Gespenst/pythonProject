import itertools

count = int(input("count = "))
str = input("str = ")

for i in itertools.product(str, repeat=count):
    res = "".join(i)
    isContains = True
    for j in str:
        if not res.__contains__(j):
            isContains = False
    if isContains:
        print(res, end=" ")
