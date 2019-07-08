massTable = '''
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186'''

import sys


class SpectrumGraph:
    def __init__(self):
        spectrum = self.readFromFile()
        massDict = self.AminoAcidMassDict()
        print(massDict)
        adj = self.constructGraph(spectrum, massDict)
        self.printResult(adj, spectrum)
        # self.saveResult(adj, spectrum)

    def readFromFile(self):
        # f = open('input.txt', 'r')
        f = [57, 71, 154, 185, 301, 332, 415, 429, 486]
        # for line in f:
        #     data = line.strip()
        spectrum = sorted([int(i) for i in f])
        # f.close()
        return spectrum

    def AminoAcidMassDict(self):
        massTable = '''
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186'''
        mass = massTable.split()
        return {int(mass[i + 1]): mass[i] for i in range(0, len(mass), 2)}

    def printResult(self, adj, spectrum):
        for i, aaList in enumerate(adj):
            for j, aa in aaList:
                print(str(spectrum[i]) + '->' + str(spectrum[j]) + ':' + aa)

    # def saveResult(self, adj, spectrum):
    #     f = open('result.txt', 'w')
    #     for i, aaList in enumerate(adj):
    #         for j, aa in aaList:
    #             f.write(str(spectrum[i]) + '->' + str(spectrum[j]) + ':' + aa + '\n')
    #     f.close()

    def constructGraph(self, spectrum, massDict):
        adj = [[] for _ in range(len(spectrum))]
        spectrum.insert(0, 0)
        for i in range(len(spectrum) - 1):
            for j in range(i + 1, len(spectrum)):
                mass = spectrum[j] - spectrum[i]
                if mass in massDict:
                    adj[i].append((j, massDict[mass]))
        return adj


if __name__ == "__main__":
    SpectrumGraph()
