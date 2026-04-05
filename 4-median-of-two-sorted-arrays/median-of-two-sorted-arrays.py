class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        merged=[]
        i=j=0

        while(i<len(a) and j<len(b)):
            if (a[i]<b[j]):
                merged.append(a[i])
                i+=1
            else:
                merged.append(b[j])
                j+=1
        merged.extend(a[i:])
        merged.extend(b[j:])
        # print(merged)
        n=len(merged)
        if(n%2!=0):
            return merged[n//2]
        else:
            return (merged[n//2]+merged[(n-1)//2])/2


       