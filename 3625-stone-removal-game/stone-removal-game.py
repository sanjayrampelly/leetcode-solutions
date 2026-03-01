class Solution:
    def canAliceWin(self, n: int) -> bool:
        stonestoberemove=10
        aliceturn=True
        while n>=stonestoberemove:
            n-=stonestoberemove
            stonestoberemove-=1
            aliceturn=not aliceturn

        return not aliceturn