class Solution:
    def majorityElement(self, a: List[int]) -> int:
        d=dict()

        for e in a:
            d[e]=d.get(e,0)+1

        for k,v in d.items():
            if v>len(a)//2:
                return k 
        