class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefixmin = 10001
        diff = 0
        for i in range(len(prices)):
            diff = max(diff, prices[i] - prefixmin)
            prefixmin = min(prices[i], prefixmin)
        return diff            



                
        
            
            
