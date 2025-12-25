class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)
        

        res = []
        for f in range(len(nums), 0, - 1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res



