class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        left, right = "", []
        for i in range(len(s)):
            if s[:i] in wordDict:
                left = left + str(s[:i])
                print(s[:i])
            if s[i:-i] in wordDict:
                left = left + str(s[i:-i])
                print(s[i:-i])
            if s[i:] in wordDict:
                left = left + str(s[i:])
                print(s[i:])
            if s[i:-i] in wordDict:

                print(s[i:-i])

        if len(left) == len(s):
            return True
        else:
            return False


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
sol = Solution()
print(sol.wordBreak(s,wordDict))


