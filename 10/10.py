def func(l1, s, l, r1, l2, r2):
    if l + l2 == s:
        print(l2, l)
        exit(0)
    elif l2 > r2:
        print("-1")
        exit(0)
    elif l + l2 < s:
        if l == r1:
            func(l1, s, l1, r1, l2 + 1, r2)
        func(l1, s, l + 1, r1, l2, r2)
    elif l + l2 > s:
        print("-1")
        exit(0)


s, l1, r1, l2, r2 = map(int, input("s, l1, r1, l2, r2 ").split())
func(l2, s, l2, r2, l1, r1)
