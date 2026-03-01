import math
class Solution:
    def trimMean(self, a: List[int]) -> float:
        a.sort()
        n=len(a)
        trimlen=math.floor(n*0.05)
        b=a[trimlen:n-trimlen]
        return sum(b)/len(b)
