class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            res.append(self.rightshift(i))

        return res



    def rightshift(self,n):
        c=0
        while(n>0):
            if(n&1):
                c+=1
            n=n>>1
        return c
