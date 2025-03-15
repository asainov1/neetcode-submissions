class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        new_s = "".join([s_i.lower().strip(" ") for s_i in s])
        new_s = re.sub(r'[^a-zA-Z0-9]', '', new_s)
        reversed_s = new_s[::-1]
        if new_s == reversed_s:
            return True
        return False
