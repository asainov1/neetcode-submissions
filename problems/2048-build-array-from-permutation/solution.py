class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        nums_2 = [0] * len(nums)
        for i in range(len(nums)):
            nums_2[i] = nums[nums[i]]
        return nums_2

