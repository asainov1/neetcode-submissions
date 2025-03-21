class Solution:
    def reverseWords(self, s: str) -> str:
        import re 
        s = s.split()
        s = s[::-1]
        return " ".join(s)
