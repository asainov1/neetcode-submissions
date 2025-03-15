class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        conc1 = "".join(word1)
        conc2 = "".join(word2)
        if conc1 == conc2:
            return True
        return False
