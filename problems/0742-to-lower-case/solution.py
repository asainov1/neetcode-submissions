class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([s_i.lower() for s_i in s])
