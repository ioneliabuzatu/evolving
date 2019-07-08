"""
Exploit overlapps amongst copies of reads from one sequence to re-assemble the original sequence
"""

# shortest common subsequence
# hamiltonian path visits each vertex once
# two reads, r1 and r2 overlap, if suffix of r1 overlaps prefix of r2
#  k > 5, as ATTAGACCTGCCGGAATAC for dummy_reads.fasta



# build the overlap tree
# weight edges -(max overlap between two reads)

class Vertex():
    pass



class Graph():
    pass



class Path():
    pass



# get the minumum-weight or maximum-weight hamiltonian path