class Solution:
    def numberOfEmployeesWhoMetTarget(self, a: List[int], target: int) -> int:
        c = 0
        for e in a:
            if e >= target:
                c += 1

        return c
