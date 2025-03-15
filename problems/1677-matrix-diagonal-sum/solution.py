class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_v = 0
        n = len(mat)
        for i in range(n):
            sum_v += mat[i][i]
            sum_v += mat[i][n - 1 - i]
        if n % 2 == 1:
            sum_v -= mat[n//2][n//2]
        return sum_v
