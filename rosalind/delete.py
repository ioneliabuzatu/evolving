def computeH(pattern):
    m = len(pattern)
    H = {1: 0, 2: 1}
    for i in range(2, m):
        j = H[i]
        bi = pattern[i - 1]
        bj = pattern[j - 1]
        while j > 0 and bi != bj:
            j = H[j]
        H[i + 1] = j + 1
    return H


def kmp(text, pattern):
    i = j = 1
    H = computeH(pattern)
    n = len(text)
    m = len(pattern)
    while i <= m and j <= n:
        while i > 0 and pattern[i - 1] != text[j - 1]:
            i = H[i]
        i += 1
        j += 1
    if i > m:
        return j - (m + 1)
    else:
        return None


def printH(H):
    for i in range(1, len(H) + 1):
        print(H[i], end=' ')


print(kmp('xxabcdabd', 'abcdabd'))
printH(computeH('abcdabd'))