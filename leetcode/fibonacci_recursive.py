from functools import lru_cache

# @lru_cache(maxsize=None)


def fibo_recursive(n, memo={}):
    # base case
    if n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        resultofN = fibo_recursive(n-1, memo) + fibo_recursive(n-2, memo)
        memo[n] = resultofN
        return memo[n]



print(fibo_recursive(5))

