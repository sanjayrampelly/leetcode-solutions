class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        for i in range(len(a)):
            if a[i] != 0:
                a[i], a[r] = a[r], a[i]
                r += 1
