class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 0
        r = 10 ** 9
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            bucket = 0
            cnt = 0 
            for i in range (len(bloomDay)): # Полу интервал
                if bloomDay[i] <= mid:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == k:
                    bucket += 1
                    cnt = 0
            if bucket >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


