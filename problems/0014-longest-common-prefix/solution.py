class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        prefix_str = ''
        for c in s:
            is_startswith_prefix = True
            for word in strs:
                if not(word.startswith(prefix_str + c)):
                    is_startswith_prefix = False
            if (not is_startswith_prefix):
                break
            prefix_str += c
        return prefix_str



