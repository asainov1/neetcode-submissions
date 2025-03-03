class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l = 0
        r = price[-1] - price[0] 
        result = 0
        while l <= r:
            m = (l + r) // 2
            last = price[0]
            count = 1
            for i in range(1, len(price)):
                if price[i] - last >= m:
                    count += 1
                    last = price[i]
            if count >= k:
                result = max(m, result)
                l = m + 1
            else:
                r = m - 1
        return result
                
