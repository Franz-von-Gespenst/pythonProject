a = int(input("число = "))
s = 0
for i in range(0, a):
    s = s + 1
    if i ** 2 >= a:
        print(i)
        exit(0)

print(s)
