class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=0
        temp=n
        while(n>0):
            rem=n%10
            rev=rem+rev*10
            n=n//10
        # print(rev)
        s=abs(temp-rev)

        return s
        