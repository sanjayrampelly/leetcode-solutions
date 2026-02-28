class Solution:
    def search(self, a: List[int], target: int) -> int:
        l=0
        r=len(a)-1

        while(l<=r):
            mid=l+(r-l)//2
            if a[mid]==target:
                return mid

            elif a[mid]>target:
                r=mid-1
            else:
                l=mid+1 

        return -1        