from collections import deque
class Solution:
    def maxDepth(self, s: str) -> int:
        cnt_1 = 0
        max_count = 0
        for c in s:
            if c == "(":
                cnt_1 += 1
            elif c == ")":
                cnt_1 -= 1

            max_count = max(cnt_1, max_count)
        return max_count
        

                
        
