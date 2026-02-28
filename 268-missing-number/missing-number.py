class Solution:
    def missingNumber(self, a: List[int]) -> int:
        n=len(a)
        s=sum(a)

        total=(n*(n+1))//2

        return total-s
        