from itertools import permutations, combinations, product
from copy import deepcopy
# red, green, blu



# first attempt
rounds = int(input())
for round in range(1, rounds+1):
    count = 0
    k,v = list(map(int, input().split()))
    colors = list(product(range(k+1), repeat=3))
    for color in colors:
        resultBinary = []
        for i in color:
            for j in color[0:]:
                if i-j <= v:
                    resultBinary.append(True)
                else:
                    resultBinary.append(False)

        if False not in resultBinary:
            count += 1

    print(count)




# solve3(k, v)
rounds = int(input())
for round in range(1, rounds + 1):
    k, v = list(map(int, input().split()))
    total = 0
    for r in range(0, v + 1):
        subtotal = 0
        for g in range(max(r - v, 0), min(r + v, k) + 1):
            minb = max(r - v, g - v, 0)
            maxb = min(r + v, g + v, k)
            subtotal += (maxb - minb + 1)
        if r == v:
            total *= 2
            total += subtotal * (k - 2 * v + 1)
        else:
            total += subtotal

    print(total)




