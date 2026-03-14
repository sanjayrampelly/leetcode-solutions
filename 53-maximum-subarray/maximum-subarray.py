class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_sum = float("-inf")

        for e in nums:
            s += e
            if s < e:
                s = e
            max_sum = max(max_sum, s)

        return max_sum
