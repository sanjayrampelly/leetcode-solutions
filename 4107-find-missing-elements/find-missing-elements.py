class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        # a.sort()
        # n = len(a)
        # res = []
        # for i in range(1, len(a)):
        #     if a[i] - a[i - 1] != 1:
        #         res.extend(range(a[i - 1] + 1, a[i]))

        # return res
        min1=min(a)
        max1=max(a)
        s=set(a)
        res=[]
        for i in range(min1,max1):
            if i not in s:
                res.append(i)
        return res