class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for ind, char in enumerate(s):
            if char_count[char] == 1:
                return ind
        return -1


