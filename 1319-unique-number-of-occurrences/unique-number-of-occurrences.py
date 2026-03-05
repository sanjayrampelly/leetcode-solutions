class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for e in arr:
            d[e]=d.get(e,0)+1

        values=d.values()
        s=set(values)

        return len(s)==len(values)
        
        