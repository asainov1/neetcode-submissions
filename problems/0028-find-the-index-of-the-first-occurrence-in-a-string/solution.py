class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if [i for i in range(len(haystack) - n + 1) if haystack[i:i+n] == needle]:
            return [i for i in range(len(haystack) - n + 1) if haystack[i:i+n] == needle][0]
        else:
            return -1

                    
        
