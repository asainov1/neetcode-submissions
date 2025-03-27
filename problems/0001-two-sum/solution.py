class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_i = {}
        for i in range(len(nums)):
            map_i[nums[i]] = i
        for i in range(len(nums)):
            v = target - nums[i]
            if v in map_i and map_i[v] != i:
                return [i, map_i[v]]

            
