class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = {}

        for num in nums1:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        res = []

        for num in nums2:
            if num in counter and counter[num] > 0:
                res.append(num)
                counter[num] -= 1

        return res


