a = int(input("число="))
b = int(input("степень="))
tempa = a
while b > 1:
    b = b - 1
    a = tempa * a
print(a)
