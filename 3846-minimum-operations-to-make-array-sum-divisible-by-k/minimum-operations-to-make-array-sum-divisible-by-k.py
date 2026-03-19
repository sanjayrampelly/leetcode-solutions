class Solution:
    def minOperations(self, a: List[int], k: int) -> int:
        c = 0
        s = sum(a)

        while s % k != 0:
            s -= 1
            c += 1

        return c
