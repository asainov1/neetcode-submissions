class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_w = 0
        for letter in string.ascii_uppercase: #set
            l = 0
            num_s = 0
            for r in range(n):
                if s[r] != letter:
                    num_s += 1
                while num_s > k:
                    if s[l] != letter:
                        num_s -= 1
                    l += 1
                w = r - l + 1
                max_w = max(max_w, w)
        return max_w

