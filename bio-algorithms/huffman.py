import sys
import os
from collections import defaultdict

DEBUG = True

# if not argument is passed, use the string as file to compress
string1 = """Huffman coding

In computer science and information theory, 
a Huffman code is an optimal prefix code found using the algorithm developed by David A. Huffman while he was a Ph.D. student at MIT, 
and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes". 
The process of finding and/or using such a code is called Huffman coding and is a common technique in entropy encoding, 
including in lossless data compression. The algorithm's output can be viewed as a variable-length code table for encoding 
a source symbol (such as a character in a file). Huffman's algorithm derives this table based on the estimated probability or frequency 
of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods,
more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, 
finding a code in linear time to the number of input weights if these weights are sorted. 
However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods.
"""

string = """qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm qwertyuiopasdfghjklzxcvbnm"""


class HuffmanEncoder:
    """
    :@ filename str
    :@ generate Distributions as dictionaries of { 'symbol': probability }
    :returns Codes as dictionaries: { 'symbol': 'codeword' }
    """

    def __init__(self, text):
        self.text = text
        self.nodes = defaultdict(int)
        self.freq_array = []
        self.freqCharacters()
        self.makeTouples()
        self.sortedFreq()

    def freqCharacters(self):
        # Get frequency of occurrence for each element
        for char in self.text:
            self.nodes[char] += 1

    def makeTouples(self):
        # generate a list of tuples and sort it in decreasing order
        self.freq_array.extend(self.nodes.items())

    def sortedFreq(self):
        self.freq_array.sort(key=lambda x: x[1], reverse=True)

    def tableCodewords(self):

        if len(self.freq_array) == 1:
            # Base case: alphabet of size 1
            x = self.freq_array[0][0]
            H = {x: ""}
            return H

        # Inductive case: alphabet of size > 1
        #    recursive call to Huffman( ) with a new A.
        else:
            x, fx = self.freq_array.pop()
            y, fy = self.freq_array.pop()
            z = x + y
            fz = fx + fy
            self.freq_array.append((z, fz))
            self.sortedFreq()
            H = self.tableCodewords()
            H[x] = H[z] + '0'
            H[y] = H[z] + '1'
            H.pop(z)
        return H


def compress(text, codewards):
    outCompressed = open("compressed.txt", "w")
    for element in text:
        outCompressed.write(codewards[element])
    outCompressed.close()


def averageBits(huffman_codes, sorted_freq):
    # get the compression ratio frequency * len(char)
    tot = sum(sorted_freq.values())
    bits = 0
    for key in sorted_freq.keys():
        bits += sorted_freq[key] * len(huffman_codes[key])
        # print(sorted_freq[key]/tot, huffman_codes[key])
    return bits


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], 'r')
        file = f.read()
        f.close()
        uncompressed_size = os.stat(sys.argv[1]).st_size
    except IndexError:
        file = string

    huffman = HuffmanEncoder(file)
    nodes = huffman.nodes
    codewords = huffman.tableCodewords()

    if DEBUG:
        print("Symbol | code")
        for k, v in codewords.items():
            print(" ", k, "\t", v)

    print("The average compression ratio is {}".format(averageBits(codewords, nodes) / sum(nodes.values())))
    # generates a file called compressed.out
    compress(file, codewords)
    print("Compression Done. Check file compressed.out")
