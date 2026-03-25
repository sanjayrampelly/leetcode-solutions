class Solution:
    def countPairs(self, a: List[int], target: int) -> int:
        c = 0
        s = set()
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] < target:
                    c += 1
        return c
