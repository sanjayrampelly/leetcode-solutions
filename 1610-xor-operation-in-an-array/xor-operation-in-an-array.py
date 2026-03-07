class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = []
        for i in range(n):
            res.append(start + 2 * i)
        x = res[0]
        for i in range(1, n):
            x ^= res[i]

        return x
