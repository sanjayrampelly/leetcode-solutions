class Solution:
    def mySqrt(self, x: int) -> int:
        # i=1
        # while i*i<=x:
        #     i+=1

        # return i-1
        l=0
        h=x

        while(l<=h):
            mid=l+(h-l)//2

            if mid*mid==x:
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                h=mid-1
        return h
        
        