import math

h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))

f1 = 60 * h1 + m1
f2 = 60 * h2 + m2

if math.fabs(f2 - f1) < 15:
    print("Встреча состоится")
else:
    print("Встреча не состоится")
