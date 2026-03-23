class Solution:
    def shuffle(self, a: List[int], n: int) -> List[int]:
        res = []
        p1 = a[:n]
        p2 = a[n:]
        for i in range(n):
            res.append(p1[i])
            res.append(p2[i])

        return res
