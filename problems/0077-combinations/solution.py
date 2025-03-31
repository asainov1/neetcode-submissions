class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        def recurs (crt, sub):
            # ... 
            if len(sub) == k:
                res.append(sub[:])
                return 
            for i in range(crt, n + 1):
                sub.append(i)
                recurs(i + 1, sub)
                sub.pop()   
        recurs (1, [])
        return res
