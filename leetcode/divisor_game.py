def game_alice(N):

    m = [False for i in range(N + 1)]

    for x in range(N):
        if (0 < x < N) and (N % x == 0) and (N - x) % 2 != 0:
            m[x] = True
    return True in m


print(game_alice(2))
