class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l =0 
        r = (len(nums) // 2 - 1 )
        ans = (len(nums) // 2)
        while (l <= r): 
            m = (l + r) // 2
            if (nums[m * 2] != nums[m * 2 + 1]):
                ans = m
                r = m - 1
            else: 
                l = m + 1
        return (nums[ans * 2])
