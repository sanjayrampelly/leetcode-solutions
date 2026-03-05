class Solution:
    def sumOfUnique(self, a: List[int]) -> int:
        d={}

        for e in a:
            d[e]=d.get(e,0)+1

        su=0
        for k,v in d.items():
            if d[k]==1:
                su+=k
            
        return su        