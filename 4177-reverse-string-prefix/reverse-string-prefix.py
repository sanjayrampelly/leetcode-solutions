class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        stack = []
        res = ""
        for i in range(k):
            stack.append(s[i])

        while len(stack):
            res += stack.pop()
        res += s[k:]
        return res
