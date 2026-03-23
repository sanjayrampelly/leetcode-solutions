class Solution:
    def stableMountains(self, a: List[int], t: int) -> List[int]:
        res = []
        for i in range(len(a) - 1):
            if a[i] > t:
                res.append(i + 1)

        return res
