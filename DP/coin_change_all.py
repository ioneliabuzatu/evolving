import numpy as np


def all_changes(coins, weight):
    # memo = [[0 for col in range(weight + 1)] for row in range(len(coins))]
    memo = np.zeros(shape=(len(coins), weight + 1), dtype=int)

    memo[:, 0] = 1

    for row in range(len(memo)):
        for col in range(1, len(memo[0])):
            if row == 0:
                if col % coins[row] == 0:
                    memo[row][col] = 1
            else:
                if coins[row] > col:
                    memo[row][col] = memo[row - 1][col]
                else:
                    memo[row][col] = memo[row - 1][col] + memo[row][col - coins[row]]

    return memo[-1][-1]


print(all_changes([2, 3, 5, 10], 15))
