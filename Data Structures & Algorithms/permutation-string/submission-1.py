class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        for left in range(len(s2) - len(s1) + 1):
            wind = s2[left:left+len(s1)]
            if target == sorted(wind):
                return True
        return False
