import numpy as np
from editdistance import edit_distance


class Align:
    """
    Given two sequences align each letter to a letter or a gap
    """

    def __init__(self, string1, string2):

        self.x = string1
        self.y = string2
        self.matrix = edit_distance(self.x, self.y)
        self.path = []  # save each step during backtracking as del, ins, or sub
        self.alignment_table = []  # use path to change strings

    def backtracking(self):
        # Backtrace is O(m + n) time, yields optimal alignment / edit transcript
        i, j = len(self.x), len(self.y)
        while i > 0 or j > 0:
            deletion = self.matrix[i - 1][j]
            insertion = self.matrix[i][j - 1]
            # substitution = self.matrix[i - 1][j - 1]

            if self.matrix[i][j] <= self.matrix[i - 1][j] and self.matrix[i - 1][j - 1] <= self.matrix[i][j - 1]:
                curr = self.matrix[i - 1][j - 1]
                self.path.append("SUB")
                i, j = i - 1, j - 1
            else:
                curr = min(self.matrix[i - 1][j], self.matrix[i][j - 1])

                # move backward
                if curr == deletion:
                    i, j = i - 1, j
                    self.path.append("DEL")
                if curr == insertion:
                    i, j = i, j - 1
                    self.path.append("INS")

    def aligning(self):
        storage = self.path[::-1]
        x = self.x
        y = self.y

        # make alignment from backtracking
        for p in range(len(storage)):
            if storage[p] == "DEL":
                y = y[:p] + "-" + y[p:]
            elif storage[p] == "INS":
                x = x[:p] + "-" + x[p:]

        self.alignment_table.append(x)
        self.alignment_table.append(y)

        return "\n".join(self.alignment_table)


if __name__ == "__main__":
    x = "AGGCTATCACCTGACCTCCAGGCCGATGCCC"
    y = "TAGCTATCACGACCGCGGTCGATTTGCCCGAC"

    a = Align(x, y)
    a.backtracking()
    print("#" * len(x) * 2)
    print(a.aligning())
    print("#" * len(x) * 2)

###############################################################
####          -AGGCTATCACCTGACCTCCAGGCCGAT--GCCC---       #####
####          TAG-CTATCAC--GACCGC--GGTCGATTTGCCCGAC       #####
###############################################################
