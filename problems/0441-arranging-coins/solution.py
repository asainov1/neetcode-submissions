class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0 
        r = n
        ans = 0 
        while (l <= r):
            m = (l + r) // 2
            if (m * (m + 1) / 2) <= n:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
