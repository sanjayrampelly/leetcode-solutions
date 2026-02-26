class Solution:
    def targetIndices(self, a: List[int], target: int) -> List[int]:

        a.sort()
        n=len(a)
        l=0
        r=len(a)-1
        index=-1

        while(l<r):
            mid=l+(r-l)//2

            if a[mid]>=target:
                r=mid
            else:
                l=mid+1
        index=l
        # print(index)
        arrindx=[]
        while( index<n and a[index]==target):
            arrindx.append(index)
            index+=1
        
        return (arrindx)
