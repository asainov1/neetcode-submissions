class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= left:
                left = last_seen[s[i]] + 1

            last_seen[s[i]] = i
            max_len = max(max_len, i - left + 1)

        return max_len
