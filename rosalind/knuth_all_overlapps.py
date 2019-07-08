class MATCHES():
    """
    Finds all overlapps of the pattern in the text using knuth-morris-pratt algorithm
    """

    def __init__(self, pattern, text):
        self.len_pattern = len(pattern)
        self.indices = []
        self.pi_func = [0 for _ in range(self.len_pattern)]  # initialize to 0
        self.compute_prefix_function(pattern)
        self.kmp_search(pattern, text)
        decoded_indeces = self.parsing_boolens(self.indices, self.len_pattern - 1)
        print(*decoded_indeces)

    # compute an array that demonstrates the longest prefix that is also a suffix for pattern
    def compute_prefix_function(self, pattern):
        m = self.len_pattern
        # pi_func = [0 for _ in range(m)]  # initialize to 0
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = self.pi_func[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
                self.pi_func[q] = k

    def kmp_search(self, pattern, text):
        m = self.len_pattern
        n = len(text)
        matches = 0
        pi_func = self.pi_func
        # print(pi_func)
        q = 0
        for i in range(n):
            while q > 0 and pattern[q] != text[i]:
                q = pi_func[q - 1]
            if pattern[q] == text[i]:
                q += 1
            if q == m:
                # print(q, m)
                matches += 1
                q = pi_func[q - 1]
                self.indices.append(True)

            else:
                self.indices.append(False)

        # add remaining Booleans (all False since pattern can't fit in remaining portion of text
        for i in range(m - 1):
            self.indices.append(False)

    def parsing_boolens(self, TF, subtract):
        output = []
        for bool in range(len(TF)):
            if TF[bool]:
                output.append((bool - subtract) + 1)
        return output


text = 'GATTAGCTTGCATTGTATT'  # input('please paste the text')
pattern = 'ATT'  # input('please paste the pattern')
matches = MATCHES(pattern, text)
