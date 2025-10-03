class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        min_length = float('inf')
        sum_l = 0
        for right in range(len(nums)):
            sum_l += nums[right]
            while sum_l >= target:
                min_length = min(min_length, right - left + 1)
                sum_l -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length
