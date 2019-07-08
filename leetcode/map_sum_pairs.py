import Trie.py


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        722222

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        count = 0
        for letter in prefix:
            if letter not in node:
                return 0
            else:
                count += 1
        return count

mapSum = MapSum()
print(mapSum.insert("a", 3))
print(mapSum.insert("app", 2))
print(mapSum.insert("apple", 9))
print(mapSum.sum("ap"))
print(mapSum.insert("b", 12))
print(mapSum.sum("a"))


# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["a",3], ["ap"], ["b",2], ["a"]]