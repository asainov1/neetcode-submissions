class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        left, right = 0, 0
        while left < len(s):
            if s[left] != t[right]:
                return False
            left += 1
            right += 1
        return True