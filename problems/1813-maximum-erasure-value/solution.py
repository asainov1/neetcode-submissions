class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        st = set()
        r = 0 
        st.add(nums[0]) # 0 element
        ans = 0
        sum_k = nums[0]
        for l in range(len(nums)):
            if l > 0:
                st.remove(nums[l-1])
                sum_k -= nums[l-1]  
            while (r + 1 < len(nums) and nums[r + 1] not in st):
                st.add(nums[r + 1])
                sum_k += nums[r+1]  
                r += 1
            ans = max(ans, sum_k) # sum otrezka
        return ans


