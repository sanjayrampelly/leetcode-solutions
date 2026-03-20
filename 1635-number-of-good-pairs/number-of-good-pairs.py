class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:

        d = {}

        for e in a:
            d[e] = d.get(e, 0) + 1

        s = 0
        for k, v in d.items():
            v -= 1
            s += v * (v + 1) // 2

        return s
