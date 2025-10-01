class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in seen:
                return [seen[sub], i]
            seen[nums[i]] = i
        return []

        
