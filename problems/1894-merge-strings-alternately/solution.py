class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = []
        word1 = [i for i in word1]
        word2 = [j for j in word2]
        while l < max(len(word1), len(word2)):
            if l < len(word1):
                res.append(word1[l])
            if l < len(word2):
                res.append(word2[l])
            l += 1
        return "".join(res)

