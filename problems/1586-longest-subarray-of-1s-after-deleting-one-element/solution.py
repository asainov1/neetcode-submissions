class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = 0 #SP O(1)
        zeroes = 0
        left = 0
        for right in range(len(nums) ): #TC O(N)
            if nums[right] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            curr_window = nums[left:right+ 1]
            max_num = max(right - left + 1 - 1, max_num)
        return max_num
                    
        

