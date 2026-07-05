class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        cnt = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                res[nums[i - 1]] = cnt
                cnt = 1
        res[nums[-1]] = cnt
        return list(sorted(res, key=lambda x: res[x], reverse=True))[:k]

            

