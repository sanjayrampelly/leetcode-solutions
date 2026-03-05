class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        s=set()
        i=0
        for e in a:
            if e not in s:
                a[i]=e
                i+=1
            s.add(e)
        return i
        