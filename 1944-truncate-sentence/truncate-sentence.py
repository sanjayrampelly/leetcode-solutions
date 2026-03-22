class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=s.split()
        ts=""
        for i in range(k):
            if i!=k-1:
                ts+=res[i] + " "
            else:
                ts+=res[i]

        return ts

        