class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        # for i in a:
        #     ele=target-i
        #     if ele in a and a.index(ele)!=a.index(i):
        #         return [a.index(ele),a.index(i)]
        d=dict()

        for i,e in enumerate(a):
            diff= target-e
            if diff in d:
                return [d[diff],i]
            d[e]=i

        