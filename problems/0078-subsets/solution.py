class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
      
        def rec_func(index, subset):
            res.append(subset)
            for i in range(index, len(nums)):
                rec_func(i + 1, subset + [nums[i]])
        rec_func(0, [])
        return res

