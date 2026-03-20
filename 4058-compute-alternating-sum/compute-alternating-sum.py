class Solution:
    def alternatingSum(self, a: List[int]) -> int:
        se = so = 0
        for i in range(len(a)):
            if i % 2 == 0:
                se += a[i]
            else:
                so += a[i]
        return se - so
