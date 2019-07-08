def fibo(n):
    memo = [-1 for i in range(n + 1)]
    memo[0] = 0
    memo[1] = 1
    for num in range(2, n + 1):
        memo[num] = memo[num - 1] + memo[num - 2]

    return memo[n]


for look_fibo in [5, 10, 15, 20, 200, 2000, 20000]:
    print(f'THe fibonacci of {look_fibo} is {fibo(look_fibo)}\t')


# Rabbits and Recurrence Relations
def rabbits(months, pairs):
    memo = [-1 for i in range(months + 1)]
    memo[0] = 0
    memo[1] = 1
    for num in range(2, months + 1):
        memo[num] = memo[num - 1] + memo[num - 2] * pairs

    return memo[months]


print(rabbits(32, 3))
