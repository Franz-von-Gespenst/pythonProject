a = int(input("число = "))

for i in range(2, a - 1):
    if a % i == 0:
        print("простое")
        exit(0)

print("не простое")
exit(0)
