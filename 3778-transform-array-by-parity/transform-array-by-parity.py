class Solution:
    def transformArray(self, a: List[int]) -> List[int]:
        for i in range(len(a)):
            if a[i] % 2 == 0:
                a[i] = 0
            else:
                a[i] = 1
        a.sort()
        return a
