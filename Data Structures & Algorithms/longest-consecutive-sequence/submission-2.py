class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = sorted(nums)
        cnt = 1
        max_o = 0
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums_s)):
            diff = nums_s[i] - nums_s[i - 1]
            if diff == 0:
                continue
            elif diff == 1:
                cnt += 1
            elif diff > 1:
                max_o = max(max_o, cnt)
                cnt = 1
        return (max(max_o, cnt))    
            