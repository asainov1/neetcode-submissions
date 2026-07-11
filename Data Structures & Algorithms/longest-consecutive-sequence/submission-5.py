class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        max_length = 0
        length= 0
        for num in nums_s:
            if num - 1 not in nums_s:
                length = 1
                while num + length in nums_s:
                    length += 1
            max_length = max(max_length, length)
        return max_length

            