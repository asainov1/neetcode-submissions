class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = [0] * 101
        for h in heights:
            counter[h] += 1
        expected = []
        for i in range(101):
            while counter[i] > 0:
                expected.append(i)
                counter[i] -= 1
         
        ans = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                ans += 1

        return ans
        

