def rabbits_dying(n, k):
    """
    :param n: Tot months
    :param k: Life spam of a rabbit
    :return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months
    R(n,m) = R(n-1)+R(n-2)-R(n-(m+1)
    """
    memo = [-1 for i in range(n + 1)]
    memo[0], memo[1] = 1, 1
    for i in range(2, n + 1):
        if i == k:
            memo[i] = memo[i - 1] + memo[i - 2] - 1
        elif i < k:
            memo[i] = memo[i - 1] + memo[i - 2]

        else:
            memo[i] = memo[i - 1] + memo[i - 2] - memo[i - (k + 1)]

    return memo[-2]


print(rabbits_dying(84, 16))

