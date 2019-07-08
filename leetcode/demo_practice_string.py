def solution(S, K):
    # write your code in Python 3.6

    S = S.upper()
    if len(S) == 1: return S
    S = S.replace("-","")

    if len(S)%K == 0:
        parts = [S[i:i + K] for i in range(0, len(S), K)]
        return '-'.join(parts)

    else:
        S = S[::-1]
        parts = [S[i:i + K] for i in range(0, len(S), K)]
        S = '-'.join(parts)
        return S[::-1]

    # return S




    # "/".join([database_letters[0]] + numbers)

# print(solution("r", 3))
print(solution("2-4A0r7-4k", 3))