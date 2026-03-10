class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        l = 0
        h = len(a) - 1

        while l < h:
            print("h", h)
            print("l", l)
            mid = l + (h - l) // 2
            print("mid", mid)
            if a[mid] > a[mid + 1]:
                h = mid
            else:
                l = mid + 1

        return l
