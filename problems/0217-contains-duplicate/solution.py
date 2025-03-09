class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums_dict = {}
        # i = 0
        # j = len(nums) - 1
        # for i in range(len(nums)):
        #     if nums[i] in nums_dict:
        #         nums_dict[nums[i]] += 1
        #     else:
        #         nums_dict[nums[i]] = 1
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        # return any([k for k in nums_dict.values() if k > 1])
