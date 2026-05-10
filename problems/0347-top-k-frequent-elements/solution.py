class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        sorted_items = sorted(count.items(),
                        key=lambda x: x[1],
                        reverse = True)
        result = []
        for i, num in sorted_items[:k]:
            result.append(i)

        return result
        
