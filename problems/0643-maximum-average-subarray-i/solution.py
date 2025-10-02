class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        wind_sum = sum(nums[:k])
        max_avg = wind_sum
        for i in range(k, len(nums)):
            wind_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, wind_sum)
        return float(max_avg) / k
    

