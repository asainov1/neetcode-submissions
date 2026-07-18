class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # i < j < k
        max_left = nums[0]
        max_diff = 0
        max_value = 0
        for i in range(1, len(nums)): 
            max_value = max(max_value, max_diff * nums[i]) #k 12
            max_diff = max(max_left - nums[i], max_diff) #j 12 , 12 
            max_left = max(max_left, nums[i]) #i 12 , 12 
        return max_value

