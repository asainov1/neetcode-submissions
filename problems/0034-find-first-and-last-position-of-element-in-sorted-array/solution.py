class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def  Binary_search (nums, target, is_searching_left):
            l = 0
            r = (len(nums) - 1)
            ans = - 1
            while (l <= r):
                m = (l + r)//2
                if (nums[m] < target):
                    l = m + 1
                elif (nums[m] > target):
                    r = m - 1
                else:
                    ans = m
                    if is_searching_left:
                        r = m - 1
                    else:
                        l = m + 1
            return ans
        left = Binary_search(nums, target, True)
        right = Binary_search(nums, target, False)
        return [left, right]
