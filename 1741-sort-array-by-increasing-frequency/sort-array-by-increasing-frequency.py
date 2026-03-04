class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:

        d = dict()

        for e in a:
            d[e] = d.get(e, 0) + 1

        a.sort(key=lambda x: (d[x], -x))

        # si=[d[x] for x in fqlist]

        # print(si)
        return a
