class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1 
        r = max(nums)
        while l <= r:
            m = (l + r) // 2
            if sum(math.ceil(i / m) for i in nums) > threshold:
                l = m + 1   #smallest divisor   
            else:
                r = m - 1
        return l 
