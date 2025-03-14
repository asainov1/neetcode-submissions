class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0 
        n = len(s)
        cnt = 0
        char_count = {'a':0, 'b':0, 'c':0}
        for r in range(n):
            char_count[s[r]] += 1
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                cnt += len(s) - r
                char_count[s[l]] -= 1
                l += 1
        return cnt
