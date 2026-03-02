class Solution:
    def findIntersectionValues(self, a1: List[int], a2: List[int]) -> List[int]:
        c = 0
        res = []
        s1 = set(a1)
        s2 = set(a2)
        for i in a1:
            if i in s2:
                c += 1
        res.append(c)
        c = 0
        for i in a2:
            if i in s1:
                c += 1
        res.append(c)
        return res
