class Solution:
    def reverseDegree(self, s: str) -> int:
        su = 0
        c = 1
        for i in range(1, len(s) + 1):
            su += (123 - ord(s[i - 1])) * i
            c += 1
        return su
