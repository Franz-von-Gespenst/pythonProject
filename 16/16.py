count = int(input())
arr = [i for i in input().split()]
if count != len(arr):
    exit(-1)
wasFound = False
for i in range(0, len(arr)):
    l = list(arr[i])
    if l[0] == "a":
        if l[4] == "5":
            if l[5] == "5":
                if l[6] == "6":
                    if l[7] == "6":
                        if l[8] == "1":
                            wasFound = True
                            print(arr[i])

if not wasFound:
    print("-1")