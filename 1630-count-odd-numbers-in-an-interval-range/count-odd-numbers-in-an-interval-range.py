class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        if low%2==0 and high%2==0:
            c= (high-low)//2

        else:
            c= (high-low)//2 +1
        return c