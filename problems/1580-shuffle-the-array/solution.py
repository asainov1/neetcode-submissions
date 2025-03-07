class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = (len(nums) // 2) 
        # nums_2 = [0] * len(nums)
        # while i < (len(nums) // 2):
        #     nums_2[2 * i], nums_2[2 * i + 1] = nums[i], nums[j]
        #     # nums_2.append(nums[i])
        #     # nums_2.append(nums[j])
        #     i += 1
        #     j += 1

        nums_2 = []
        for i in range(len(nums) // 2):
            nums_2.append(nums[i])
            nums_2.append(nums[j])
            j += 1
        return nums_2
