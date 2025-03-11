class Solution:
    def replaceDigits(self, s: str) -> str:
        ind_dict = {}
        s = list(s)
        for idx, letter in enumerate(string.ascii_lowercase):
            ind_dict[idx] = letter
        for s_i in range(len(s)):
            if s_i % 2 != 0:
                s[s_i] = chr(ord(s[s_i - 1]) + int(s[s_i]))
        return "".join(s)
            

