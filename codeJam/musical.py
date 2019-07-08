from itertools import combinations, permutations
import numpy as np
#
# Input
#
# 3
# 2
# 0.2500 0.5000 0.5000 0.2500
# 3
# 0.0000 0.0000 0.0000 0.0009 0.0013 0.1776

#
# (1 - (0.2500 * 0.5000)) *  (1-(0.5000 * 0.2500))
#
# (1-(0.0000* 0.0000))*(1-(0.0000 * 0.0009)) * (1-(0.0013 *0.1776))

def quicksort(probs):

    left, right, middle = [], [], []

    if len(probs) > 1:

        pivot = probs[-1]
        for n in probs:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                middle.append(n)

        return quicksort(left) + middle + quicksort(right)
    else:
        return probs


def maxsuccess():
    output = {}
    for repeat in range(1, int(input()) + 1):

        out = []
        roles = int(input())
        probabilities = [float(x) for x in input().split()]
        probabilities = quicksort(probabilities)
        while len(probabilities) > 1:
            p = (1 - (probabilities[0] * probabilities[-1]))
            out.append(p)
            del (probabilities[0])
            del (probabilities[-1])
        f =out[0]
        for i in out[1:]:
            f = f*i
        output[repeat] = "Case #" + str(repeat) + ":" + " " + str(f)
        print(out)
    return "\n".join(output.values())


# print(maxsuccess())

text = (n.strip() for n in """
3
2
0.2500 0.5000 0.5000 0.2500
3
0.0000 0.0000 0.0000 0.0009 0.0013 0.1776
1
1.0000 0.1234
""".split('\n')[1:])
input = lambda: next(text)

