"""
A search Trie for the KMP algorithm. For on string only or text without spaces in between.
"""


from collections import defaultdict


class SuffixTrie():
    def __init__(self, textNospces):
        textNospces += "$" # flag the end of the string
        self.root = defaultdict()
        loopEnd = 0
        while loopEnd < len(textNospces):
            current = self.root
            for char in textNospces[loopEnd:]:
                if char not in current:
                    current[char] = {}

                current = current[char]
            loopEnd +=1

    def path(self, pattern):
        root = self.root
        for char in pattern:
            if char not in root:
                return None
            root = root[char]
        return root

    def substring(self, pattern):
        return self.patternPath(pattern) is not None


if __name__ == "__main__":
    trie = SuffixTrie("TGATATAGACATCTTA")
    # patterns = ["ATAGA", "ATC", "GAT"]
    print(trie.substring("GAT"))