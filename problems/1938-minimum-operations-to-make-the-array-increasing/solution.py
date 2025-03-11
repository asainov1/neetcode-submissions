class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l, j = 0, len(nums) - 1
        ans = 0
        cnt = 0
        mn = nums.copy()
        # mn[0] = nums[0]
        for i in range(1, len(nums)):
            # diff = (nums[i -1] - mn[i] + 1) 
            if nums[i -1] >= nums[i]:
                diff = (nums[i -1] - mn[i] + 1)     
                nums[i] += diff
                cnt += diff
        return cnt 
        
                

            

