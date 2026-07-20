class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        cnt = 0
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    cnt += 1
            res.append(cnt)
            cnt = 0
        return res
