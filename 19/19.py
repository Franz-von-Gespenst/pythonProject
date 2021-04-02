from itertools import combinations
L = [1, 2, 3, 4]
print([",".join(map(str, comb)) for comb in combinations(L, 3)])
