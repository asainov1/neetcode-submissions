class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = len(prices) - 1
        max_num = max(prices)
        ans = 0
        mn = [0] * len(prices)
        mn[0] = prices[0]
        for i in range(1, len(prices)):
            mn[i] = min(mn[i-1] , prices[i])
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - mn[i-1])
        return ans

            
            
