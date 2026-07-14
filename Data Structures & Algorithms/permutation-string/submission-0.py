class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for left in range(len(s2) - len(s1) + 1):
            wind = s2[left:left+len(s1)]
            if sorted(s1) == sorted(wind):
                return True
        return False
