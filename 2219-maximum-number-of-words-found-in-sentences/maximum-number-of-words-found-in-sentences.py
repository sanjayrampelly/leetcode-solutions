class Solution:
    def mostWordsFound(self, a: List[str]) -> int:
        l=0
        for e in a:
            l=max(l,len(e.split()))

        return l