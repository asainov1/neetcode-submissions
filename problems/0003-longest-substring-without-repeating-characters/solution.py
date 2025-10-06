class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_set = set()
        left = 0
        max_set =0
        for right in range(len(s)):
            while s[right] in s_set:
                s_set.discard(s[left])
                left += 1
            s_set.add(s[right])
            max_set = max(len(s_set), max_set)
        return max_set
