def func(x0, v0, t):
    g = 9.8
    return x0 + (v0 * t) - (g * t * t / 2)


x0, v0, t = map(float, input("x0, v0, t ").split())
print(func(x0, v0, t))
