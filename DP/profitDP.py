import numpy as np


def profit(prices, k):
    if k == 0 or not prices:
        return 0

    diff = [-55] * k
    m = [-50] * (len(prices) - 1)
    l = 0

    for i in range(len(prices)):
        for j in prices[i + 1:]:
            print(j, " - ", prices[i], "=", j - prices[i])
            m[l] = max(m[l], j - prices[i])
        l += 1
        print("===================")

    m1 = [i for i in m if i > 0]
    if m1:
        m1 = max(m1)
        m.remove(m1)
    m2 = [i for i in m if i > 0]
    if m2:
        m2 = max(m2)

    return (m1 if m1 else 0) + (m2 if m2 else +0)


# print(profit([3, 2, 6, 5, 0, 3], k=2))
print(profit([2, 3], k=2))
