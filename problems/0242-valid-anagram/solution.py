from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)
        counter_2 = Counter(t)
        for num in t:
            if num not in counter:
                return False
        if counter_2 != counter:
            return False
        return True

