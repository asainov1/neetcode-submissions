class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        res = re.search(rf'^{p}$',s)
        if res:
            return True
        return False
        
