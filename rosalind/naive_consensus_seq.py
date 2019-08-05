from readparse_FASTA import ReadFASTA
from numpy import zeros


def strings_dna(filename):
    with open(filename, 'r') as file:
        f = file.read()
        all = filter(None, f.split('>'))
        matrix_strings = []
        for single in all:
            single = single.split('\n')
            # print(single[1])
            matrix_strings.append(single[1])
    return matrix_strings, len(single[1])


def parsing_matrix(matrix, len_fasta):
    A, C, G, T = [0 for i in range(len_fasta)], [0 for i in range(len_fasta)], [0 for i in range(len_fasta)], [0 for i
                                                                                                               in range(
            len_fasta)]

    for row in range(len(matrix)):
        # print(matrix[row])
        for col in range(len(matrix[0])):
            # print(matrix[row][col])
            if matrix[row][col] == 'A':
                A[col] += 1

            elif matrix[row][col] == 'C':
                C[col] += 1

            elif matrix[row][col] == 'G':
                G[col] += 1

            elif matrix[row][col] == 'T':
                T[col] += 1

    return A, C, G, T


def find_consensus(A, C, G, T, len_fasta):
    output_num = [0 for i in range(len_fasta)]
    output_string = ''
    for cons_max in range(len_fasta):
        output_num[cons_max] = max(A[cons_max], C[cons_max], G[cons_max], T[cons_max])
        if A[cons_max] >= C[cons_max] and A[cons_max] >= G[cons_max] and A[cons_max] >= T[cons_max]:
            output_string += 'A'

        elif C[cons_max] >= A[cons_max] and C[cons_max] >= G[cons_max] and C[cons_max] >= T[cons_max]:
            output_string += 'C'

        elif G[cons_max] >= A[cons_max] and G[cons_max] >= C[cons_max] and G[cons_max] >= T[cons_max]:
            output_string += 'G'

        elif T[cons_max] >= C[cons_max] and T[cons_max] >= G[cons_max] and T[cons_max] >= A[cons_max]:
            output_string += 'T'

    assert len(output_string) == len_fasta
    print(len(output_string), len_fasta)
    return output_string


def naive_():
    dna_list = ReadFASTA('../data/MA0059.1.txt')
    # Setup an array and count into the array
    M = zeros((4, len(dna_list[0][1])), dtype=int)
    snp_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for dna in dna_list:
        for index, snp in enumerate(dna[1]):
            M[snp_dict[snp]][index] += 1
    # Determine the consensus string
    consensus = ''
    to_snp = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    for i in range(0, len(dna_list[0][1])):
        maxval = [-1, -1]
        for j in range(0, 4):
            if maxval[1] < M[j][i]:
                maxval = [j, M[j][i]]
        consensus += to_snp[maxval[0]]
    # Format the count properly
    consensus = [consensus, 'A:', 'C:', 'G:', 'T:']
    for index, col in enumerate(M):
        for val in col:
            consensus[index + 1] += ' ' + str(val)
    # Print and write the output
    print('\n'.join(consensus))
    with open('010_CONS.txt', 'w') as output_data:
        output_data.write('\n'.join(consensus))


naive_()
# file_name = '/Users/ioneliabuzatu/Downloads/rosalind_cons.txt'
# matrix, len_fasta = strings_dna(file_name)
# A, C, G, T = parsing_matrix(matrix, len_fasta)
# consensus_sequence = find_consensus(A, C, G, T, len_fasta)
# print(consensus_sequence)
# print(*A)
# print(*C)
# print(*G)
# print(*T)
# ATGCAACT
