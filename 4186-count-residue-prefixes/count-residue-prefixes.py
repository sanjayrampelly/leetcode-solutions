class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        pre = ""
        c = 0
        for ch in s:
            pre += ch
            seen.add(ch)
            if len(seen) == len(pre) % 3:
                c += 1
        return c
