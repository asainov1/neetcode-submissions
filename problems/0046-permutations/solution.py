class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(ind):
            if ind == len(nums):
                res.append(nums.copy())
            for i in range(ind, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]
                back(ind+1)
                nums[i], nums[ind] = nums[ind], nums[i]

        back(0)
        return res
