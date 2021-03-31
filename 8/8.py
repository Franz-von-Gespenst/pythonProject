a, s, b = map(str, input().split())

try:
    a = float(a)
    b = float(b)
except ValueError:
    print("НЕподходящее значение")
    exit(-1)
    
if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
elif s == "/":
    if b == 0:
        print("Деление на 0")
        exit(-1)
    print(a / b)
else:
    print("Неподходящий символ")
    exit(-1)
