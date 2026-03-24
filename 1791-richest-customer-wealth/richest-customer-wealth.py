class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        s=0
        for i in a:
            s=max(sum(i),s)
        return s        