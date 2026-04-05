class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        merged = []
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        
        merged.extend(a[i:])
        merged.extend(b[j:])
        
        n = len(merged)
        ans = 0

        if n % 2 != 0:
            ans = merged[n // 2]
        else:
            ans = (merged[n // 2] + merged[(n - 1) // 2]) / 2
        return ans
