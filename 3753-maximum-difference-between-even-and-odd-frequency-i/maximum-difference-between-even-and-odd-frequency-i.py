class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        maxodd = 0
        maxeven = float("Inf")
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for i in d.values():
            if i % 2 == 0:
                maxeven = min(maxeven, i)
            else:
                maxodd = max(maxodd, i)

        return maxodd - maxeven
