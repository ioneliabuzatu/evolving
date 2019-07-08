def recString(s):
    return recString(s[::-1])



s = ["H", "a", "n", "n", "a", "h"]
print(recString(s))