import numpy as np


def spi(pattern):
    pi = np.zeros(shape=(len(pattern)), dtype=int)
    i = 1
    while i < len(pattern):
        if pattern[i] in pattern[:i]:
            pi[i] = max(pi) + 1
            i += 1
        else:
            pi[i] = 0
            i += 1
    return pi


def kmp(seq, pattern):
    shifts_after_nonANDmatch = spi(pattern)
    index_seq = 0
    index_pattern = 0
    all_matchs = []
    while index_seq < len(seq):
        seqid = seq[index_seq]
        pattid = pattern[index_pattern]
        if seq[index_seq] == pattern[index_pattern]:
            index_seq += 1
            index_pattern += 1
        else:
            if seq[index_seq] != pattern[index_pattern] and index_pattern != 0:
                shift = (index_pattern + 1) - shifts_after_nonANDmatch[index_pattern]
                index_seq = index_seq + (index_seq - shift)
                index_pattern = 0

            else:
                index_seq += 1

        if index_pattern == len(pattern) - 1:
            check = index_seq - (len(pattern)) + 2
            all_matchs.append((index_seq - (len(pattern)) + 2))
            # index_seq = (index_seq - len(pattern)) + 2
            # index_seq = index_seq - 1
            shift = (index_pattern + 1) - shifts_after_nonANDmatch[index_pattern]
            index_seq = index_seq + (index_seq - shift)
            index_pattern = 0

    return all_matchs


def dummy_kmp(mRNA, pattern):
    for i in range(len(mRNA)):
        pass


# print('abababca')
# print(spi('abababca'))
# print(spi('atat'))

mRNA = 'AUAGCUAUCAGAAAGGUACUUACG'
pattern = 'UA'
print(kmp(mRNA, pattern))
print(kmp_2(mRNA, pattern))
