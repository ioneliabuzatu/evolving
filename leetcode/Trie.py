# takes in a list of words
# def make_trie(*words):
#     # creates our root dict()
#     trie = dict()
#
#     for word in words:
#         # create a temporary dict based off our root
#         # dict object
#         temp_dict = trie
#
#         for letter in word:
#             # update our temporary dict and add our current
#             # letter and a sub-dictionary
#             temp_dict = temp_dict.setdefault(letter, {})
#
#         # If our word is finished, add {'*': '*'}
#         # this tells us our word is finished
#         temp_dict["#"] = "#"
#     return trie
#
#
# # Test our trie creation
# trie = make_trie('hi', 'hello', 'howdy')
# # print out our new trie
# print(trie)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word: #make a dictionary with unique starting letter and add subdictionaries ending with "end
            node = node.setdefault(letter, {}) # dict + subdictionary
        node["end"] = "end" # to check later word ending

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter in node:
                node = node[letter]
            else:
                return False
        return "end" in node


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()

print(trie.insert("apple"))
print(trie.search("apple"))   # returns true
print(trie.search("app"))    # returns false
print(trie.startsWith("app")) #  returns true
print(trie.insert("app"))
print(trie.search("app"))    # returns true
print(trie.startsWith("helloa"))

