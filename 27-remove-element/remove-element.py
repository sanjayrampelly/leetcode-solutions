class Solution:
    def removeElement(self, a: List[int], val: int) -> int:
        r = 0
        # j=len(a)-1

        for i in range(len(a)):
            if a[i] != val:
                a[i], a[r] = a[r], a[i]
                r += 1

        return r
