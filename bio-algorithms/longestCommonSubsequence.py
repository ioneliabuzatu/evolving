"""Different styles for the longest common subsequence"""

import numpy as np


def lcs(string1, string2):
    """
    :param string1:
    :param string2:
    :return: the longest common subsequence
    :with top down approach
    """

    if not string1 or not string2:
        return []

    # matrix = [["" for i in range(len(string2))] for j in range(len(string1))] # row and columns of empty matrix

    matrix = np.empty(shape=(len(string1), len(string2)), dtype='<U255')

    for row in range(len(string1)):
        for col in range(len(string2)):
            if string1[row] == string2[col]:  # if they are equal extended by that element
                matrix[row][col] = matrix[row - 1][col - 1] + string1[row]

            else:  # if they are not equal get the max by key = len
                matrix[row][col] = max(matrix[row][col - 1], matrix[row - 1][col]) + "_"

    lcs = matrix[-1][-1]
    # print(matrix)
    return lcs


def lcs_index(s1, s2):
    matrix = np.empty(shape=(len(s1), len(s2)), dtype="<U255")
    i, j = 0, 0
    while i < len(s1):
        if s1[i] == s2[j]:
            matrix[i, j] = matrix[i - 1][j - 1] + s1[i]  # take the diagonal
            j += 1
        else:
            matrix[i, j] = max(matrix[i - 1, j], matrix[i, j - 1]) + "_"  # chose le longest between upper right or leftwards symbol
            j += 1
        if j == len(s2):  # end of row
            i += 1
            j = 0

    return matrix[-1, -1]


def lcs_recursive(string1, string2):
    """
    :param string1:
    :param string2:
    :return: longest common subsequence recursively
    """
    if not string1 or not string2:
        return ""

    string10, string11, string20, string21 = string1[0], string1[1:], string2[0], string2[1:]

    if string10 == string20:
        return string10 + lcs(string11, string21)  # if equal extended

    else:
        return max(lcs(string1, string21), lcs(string11, string2), key=len)  # if not equal


string1 = "abcdef"
string2 = "abef"
t = "TAGCTATCACGACCGCGGTCGATTTGCCCGAC"
s = "AGGCTATCACCTGACCTCCAGGCCGATGCCC"
X = "aaaaaaabbbbbbb"
Y = "bbbbbbbccccccc"

# print(lcs(t,s) + "\n" + t)
# print(lcs(X, Y) + "\n" + X)
print(t + "\n" + lcs_index(t, s))
