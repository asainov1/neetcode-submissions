class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = 0
        for val in nums:
            tmp ^= val

        return tmp
        
