class Solution:
    def getSneakyNumbers(self, a: List[int]) -> List[int]:
        s=set()
        res=[]

        for e in a:
            if e in s:
                res.append(e)
            s.add(e)

        return res