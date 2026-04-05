class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        temp = x
        sign = 1
        if temp < 0:
            sign = -1
            temp = abs(temp)

        while temp > 0:
            rem = temp % 10
            rev = rev * 10 + rem
            if rev < -(2**31) or rev > 2**31 - 1:
                return 0
            temp = temp // 10

        return rev * sign
