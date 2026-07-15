from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        q = deque()
        b = deque()
        for c in s:
            if c == "#":
                if q:
                    q.pop()
            else:
                q.append(c)
        
        for c in t:
            if c == "#":
                if b:
                    b.pop()
            else:
                b.append(c)
        return q == b
