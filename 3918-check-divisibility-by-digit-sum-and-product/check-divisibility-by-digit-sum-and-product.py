class Solution:
    def checkDivisibility(self, n: int) -> bool:
        t=n
        s=0
        p=1
        while(n>0):
            rem=n%10
            s+=rem
            p*=rem
            n//=10
        print(s,p,t//(s+p))

        return t%(s+p)==0