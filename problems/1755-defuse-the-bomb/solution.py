class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []

        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            elif k < 0:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            else:
                total = 0
            res.append(total)
        
        return res

