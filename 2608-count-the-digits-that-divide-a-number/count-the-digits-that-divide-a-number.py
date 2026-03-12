class Solution:
    def countDigits(self, n: int) -> int:
        c=0
        temp=n

        while(n>0):
            rem=n%10
            if(temp%rem==0):
                c+=1
            n//=10

        return c

        

