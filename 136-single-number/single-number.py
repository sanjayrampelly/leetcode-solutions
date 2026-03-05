class Solution:
    def singleNumber(self, a: List[int]) -> int:
        if len(a) == 1:
            return a[0]

        d = {}

        for e in a:
            d[e] = d.get(e, 0) + 1

        for k, v in d.items():
            if d[k] == 1:
                return k
