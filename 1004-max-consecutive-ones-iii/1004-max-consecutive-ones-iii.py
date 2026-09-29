class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l =  0
        left_k = 0
        max_ones = 0
        """
        [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
                   l               r
        left_k = 2
        max_ones = 
        """
        for right in range(len(nums)):
            if nums[right] == 0:
                left_k += 1
            while left_k > k:
                if nums[l] == 0:
                    left_k -= 1
                l += 1

            max_ones = max(max_ones, right - l + 1)
            print (max_ones)

        return max_ones