class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res, l, r = [], 0, n
        while l < (n): # a > b else a = b , a < b  ;  l > n l = n else l < n
            res.append(nums[l])
            l += 1
            res.append(nums[r])
            r += 1
        print(l, r)
        return res
