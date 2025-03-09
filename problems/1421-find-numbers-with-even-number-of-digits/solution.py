class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        cnt = 0
        while l <= r:
            num = len(str(nums[l])) 
            if int(num) % 2 == 0 :
                cnt += 1
            l += 1
        return cnt



