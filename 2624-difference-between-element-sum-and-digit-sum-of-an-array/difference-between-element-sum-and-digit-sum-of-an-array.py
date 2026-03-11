class Solution:
    def differenceOfSum(self, a: List[int]) -> int:
        asum=sum(a)
        esum=0
        for e in a:
            if e>9:
                rem=0
                s=0
                while(e>0):
                    rem=e%10
                    s+=rem
                    e//=10
                esum+=s
            else:
                esum+=e

        return abs(esum-asum)
