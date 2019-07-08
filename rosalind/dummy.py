def count_deoxy(seq):
    """
    :param seq: DNS sequence
    :return:  'A', 'C', 'G', and 'T'  count
    """
    A, C, G, T = 0, 0, 0, 0

    for deoxy in seq:
        if deoxy == 'A':
            A += 1
        elif deoxy == 'C':
            C += 1
        elif deoxy == 'G':
            G += 1
        else:
            T += 1

    return A, C, G, T


# seq = 'CCATGAATCTTCGTAGAGCAGACGCTACCACCATTGTCAATTGGTCAACTATAAGCCTCCGATAGAGCCTTACCCTCCGATCCCAACCGTGCGTACAAATGCTGTGAGACATTAAAATAAGACATCCTTCTACGGAGGGAATAAGGACGCTGGCTCCCATTGGGTTGAGCCCATAAAACGTGGGAACTTGCGGGTTGTCCGTTCTGGAACGTGACACTTAAGTGAACATCTATTCCAAGAGGCATCCCTCCAGGAGGAATCGATTGCTAGTGCACTAATGCTCCGAGTGTGGCAATTGAATGCCAGCAGACGACGCTAAGCCGAATCTTCCGGCTCATAGTTCTCCACTGGCGGCCGCGTTTGGTCTGGGGAATCCCGGAACACCCAGCTGAGCGGTGTAGGTGTAGCGAGGATTTTGAACTCGTGATGCGCCTCTTGTCCACAACAACGATGGAGGGAAAGCAGGTATAAATTTCCCACCCTTTGATATGCGTCTCTTCCCCTACACGTTTGGAGAAACACACCAAGGCGATATATATACTTACCTGAGTGCATGGTCTACGGCCTACCCAGTCTGCGAGTGCTCGCGGTTCCCCTATTATTGTCTATCAGCACGTCATAAGGATGAGCTGAAAGGTGTAAAATACATAGCGAAACTACTGCACAATCGAGTTTCCCACTATGATGTCGACCTATGACCTGCCTCTCCCGCTCCTGAGCCGATAGTCTGCAGTCAGAGTGGTGGCCGCTTTCACAATGCGTAAGCAGTAGCCTTATACGTTGCTTCGTATCCATAGCGGGTACCT'
# print(count_deoxy(seq))


def dna_to_rna(dna):
    rna = ''
    for i in range(len(dna)):
        if dna[i] == 'T':
            rna += 'U'
        else:
            rna += dna[i]

    return rna


# dna = 'TTATGTTGAAATGTAGTGTCTCGTACACGCATTTCAAAGAAGGAGCGGGCGCATATAGTGAGCCAACCCGAGGTGTACAGAGCGCGATGGCTAAGAAAGCATATTACTAAGGGGACCGGAGGTGGTCCATGCATCCGGAACTAGAGATGGTGATATACGACCTAAGCTCACCGCCTCCGGACAGTTATCCAGAGACTGTTCTTTAGGGTTTCTAAGGGGGGTTGCGAACTCACAGGACATCGGTAGTAGCTACGTTTAGCCACGCTGTCCGTTTGATCTACCAATGCTTTCTGGAAGCACAGACTCTCTAGGGTGGGCATCATCAGCGTAAAAAGGATGAGGCATCCGCCACAGGACGACACTTGGGTTGTTCACTCGGTAGGGTCGGCGCAATCCGCTTGACTTGTCGCATAGCTCTAGTAGCGCTACGGGCTCTTAAACTCACTAGCGGGCCTAAGTCCCAGCCCGAGCGTAGCACCTTGATTCCAGATCCCTTTAATTAGACTTCGTTATGGCAATGCAACACGGTTCTTATTAAGCGGAACAATCATCAGTTTTTAGAAACACATTGCACCCACTTAAAGTGGGCTTTACGGCCTCCGTGTTTTCTGTCACTAACGGTCTTCTCCAGTTACAAGCGTGTCTGCCCTCTAATGCTACATCGAGACGTGCGACCCCCATGAGCTACAAGCTTTAATGGTGAAGCGCCCTACCGTAATGTCTCAATTTTCTAAGTAGCAGCATGCCCTTCCGTGGATTGGGCTTTAGCTATCCAGGATCAACACAGTTCCAAGGAACAAATGGTTGTCATATATCGGATTTTATTTCGTAAAAACAAGTAAAGTACCGGCGTTCCACGAATTGCATGAGAAGTGCCAACTCAGTAATCAACTTTAACTCACAGCTCGAAGGATATAATCCAGTACTTCGCTTTCCTACGTTTGGACTTCCCACGGTCTGATGTGCTTTCATAGGGTTGTTGTGACCATTACGAGCGATT'
# print(dna_to_rna('GCGACCCGGAAACCAGGGCAGATAGCAATCCAGGAATGATTGACGTGTTGTTTCTCCCGAAAGGAGCCTCCTTGGGCCCGATCAAGCACGCCGCCCAACCCATGTAATGGGTCCACTTTCTAGAGGGTACTGGAGGATCAATTCTATCCACGACGATCCATTATTAGCGTTGCCTTGTACAAGAACGTAATCCAATCTAATGGAATAGTATTTTCTCTAGCTGAAAGTGGTCCCATCTATTCCAGGTCTAGCTAGACACAGCGTGGAAGGCACCGGGGTCACTAGTTTGACAATGGCGGAATGTCAGGTATCGCGTAGTGTGTTACCACTCCCGACTACTATGCTATTGCTGAAACCCGGTAGTGAGACTACCCCGAGCGTTGCTACGGTATATTCCCACTTATGCGGCTAGGCATACCTCACTATTTCTGCCAACCTATACGTCTACCATCCGTAGTCCAGTACGGTGATGAGGGCCTTGCGCATACGGGCACTACCACATACACTCCGTCGCCGCATCAAATTTTCTCACCAGCCAAATTGTGGATGTTATTCTGCAGTCATGAGTTGCATAGTCCCGCGGCTTCGAGATAGTTACATCTACTAATATTAGTACCACAGCGAGTAACATCGCTCGCCCTCTCTCGTGCGCTCGACGTAGTACCCGGCGTCCTACGGCAATACCCGCGTCCGATCCATAAGCATTGTTCATCATCCAGTGTATACTCATAACCAGCCTAACAGGGCCGCCGTAGTAGGGTATCCCACAGTGAATACGGGGGATCAATTAGTTGGTTTAAACAGTCAAGAACCCTGTCGAGCGCCCAGCGTATCTCGCTAACAATAGGGGTCGGAAGCGGCCGTTGGCGGCCACCAAATTTAGGATGAATTTTATAGCTAGT'))


def reverse_complpement(forward):
    rev_com = ''
    for deoxy in forward[::-1]:
        if deoxy == 'A':
            rev_com += 'T'
        elif deoxy == 'C':
            rev_com += 'G'
        elif deoxy == 'G':
            rev_com += 'C'
        else:
            rev_com += 'A'
    return rev_com


# forward = 'AAAACCCGGT'
# print(reverse_complpement('GTAACGGGCCTACGAACTAACGACTAGTATACTCTATCCTCCTTAAGTCAACCACGAAACTGCGGAGGCCCATATCATCTTGAGAACATGCTCACCCTAGCTCGTCGCGAATCCCCACAACGTGAGGGACAGTACCTACAAATAAGATGCCAGTAGAACCCCCAGAGTAGCGCCAGATCTCCTTTGAATTCTACTGGAATTAACGTTTCCAAAGTCCTCGCAGATATACGGGCCCGCAGTGATCCGGTGCACTGAGCGACACATATCACCCGGTCACATCCTTCACTCCGCTAGAGATCAACCGGGTTCTGGTAGTTTCAAGGCTATTTACTTATCCAAACACCCGAAGAAGTCTTTTCGGCGCGATCGCCCCAGACCGTGAGAATTGTCATACGTGCGCGCTACCAATTACTATTTTTATTGACTGCACTGTCCGGTACCATGACAGCTGGGTTAAGAGTATAGGAATGAAGTTAAGCTGCTGCCACCGTCTGATAACAGAAGATCAATGCCCACCGGTACGTACGCTGTATTGGGTTCCTCAGCAATCCACCATTAAAAACGTGTAGTTTTGGAGTCCATATTGATTAACCCGTAGATTGTGAACGGTCCTCCGAGGACACTCGAGCTATGGCGATTACCCCCTCGATACAGACAGAACCGCGCCGGCGAGAGGGAGAGTAACAAAGGAGACAGACCCACACTAGCGAACACTTAGACGTTCTATAACCTTTGCCTTAATTTATCGGATCAACCTAGCGAAGTCCCTGAACGATGGGAGGTGTATACGCCGGGGATATGACATTGAAGCCGGCGCGAGTTGACTGGGCTGACGTCTACCAGTTGGTAGCGGGTCT'))


def hammington(seq1, seq2):
    point_mutations = 0
    for s1, s2 in zip(seq1, seq2):
        if s1 != s2:
            point_mutations += 1
    return point_mutations


# print(hammington(hammington_seq1, hammington_seq2))

def file_hammington():
    with open('/Users/ioneliabuzatu/Downloads/rosalind_hamm.txt', 'r') as file:
        seq1_2 = []
        f = file.read()
        for ham in f.split('\n'):
            seq1_2.append(ham)
            # print(ham)
            # print(str(ham.split(' ')))
    return seq1_2


seq12 = file_hammington()
hammington_seq1 = seq12[0]
hammington_seq2 = seq12[1]


# print(hammington(hammington_seq1, hammington_seq2))


# File.open('data/rosalind_iprb.txt', 'r') do |f|
# arr = f.readlines[0].gsub("\n", '').split().collect(&:to_i)

def mendel(k, m, n):
    total_pop = k + m + n
    total_probability = ((k ** 2 - k) + (2 * k * m) + (3 / 4 * (m ** 2 - m)) + (2 * k * n) + (m * n)) / (
            total_pop ** 2 - total_pop)
    return total_probability


print(mendel(2, 2, 2))
print(mendel(23, 24, 30))
