import math

k = int(input("1 or 2 "))
if k == 1:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("s = ", s)
elif k == 2:
    x1, x2 = map(float, input().split())
    y1, y2 = map(float, input().split())
    z1, z2 = map(float, input().split())
    s = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) + math.pow((z1 - z2), 2))
    print("s = ", s)
else:
    print("error")