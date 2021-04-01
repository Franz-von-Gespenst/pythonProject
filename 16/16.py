count = int(input())
arr = [str(i) for i in input().split()]
if count != len(arr):
    exit(-1)
wasFound = True
for i in range(0, len(arr)):
    l = list(arr[i])
    if l[0] == "a":
        if l[4] == "5":
            if l[5] == "5":
                if l[6] == "6":
                    if l[7] == "6":
                        if l[8] == "1":
                            wasFound = False
                            print(arr[i])

if wasFound:
    print("-1")