import numpy as np


def edit_distance(string1, string2):
    """
    :get minimum of four possible cases: D[i, j-1]+1, D[i-1, j]+1, D[i-1,j-1]+1, D[i,j]
    :param string1: type str
    :param string2: type str
    :return: mimimum operation to have equal strings in O(len(string1)*len(string2))
    """

    if not string1:
        return len(string2)
    elif not string2:
        return len(string1)

    matrix = np.zeros(shape=(len(string1) + 1, len(string2) + 1), dtype=int)
    backtrace = np.zeros(shape=(len(string1) + 1, len(string2) + 1), dtype=int)

    matrix[:, 0] = range(1 + len(string1))  # if string2 is empty
    matrix[0, :] = range(1 + len(string2))  # if string1 is empty

    for i in range(1, 1 + len(string1)):
        for j in range(1, 1 + len(string2)):

            # check all four subcases and get the minimum
            deletion = matrix[i - 1][j] + 1
            insertion = matrix[i][j - 1] + 1
            substitution = matrix[i - 1][j - 1] + (1 if (string1[i - 1] != string2[j - 1]) else 0)
            matrix[i][j] = np.min([deletion, insertion, substitution])

            # store backtracking
            if matrix[i][j] == deletion:
                backtrace[i][j] = 1  # "DEL"
            elif matrix[i][j] == insertion:
                backtrace[i][j] = 2  # "INS"
            else:
                backtrace[i][j] = 3  # "SUB"

    return matrix


x = "intention"
y = "execution"

print("The edit distance between '{}' and '{}' is {}".format(x, y, edit_distance(x, y)))
