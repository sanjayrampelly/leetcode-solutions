class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        a.sort()
        n=len(a)
        res=[]
        for i in range(1,len(a)):
            if a[i]-a[i-1]!=1:
                res.extend(range(a[i-1]+1,a[i]))

        return res

