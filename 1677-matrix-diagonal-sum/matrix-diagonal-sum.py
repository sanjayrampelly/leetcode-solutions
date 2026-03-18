class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        for i in range(len(mat)):
            s += mat[i][i]
            s += mat[i][n - i - 1]
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s
