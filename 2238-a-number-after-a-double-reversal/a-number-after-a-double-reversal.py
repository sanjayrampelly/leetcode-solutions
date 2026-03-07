class Solution:
    def isSameAfterReversals(self, n: int) -> bool:
        org = n
        rev = 0
        while n > 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10
        # print(rev)
        rev1 = 0
        while rev > 0:
            rem = rev % 10
            rev1 = rev1 * 10 + rem
            rev = rev // 10
        # print(rev1)
        return org == rev1
