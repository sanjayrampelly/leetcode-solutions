class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for e in s:
            d[e] = d.get(e, 0) + 1

        print(d)

        for i, e in enumerate(s):
            if d[e] == 1:
                return i

        return -1
