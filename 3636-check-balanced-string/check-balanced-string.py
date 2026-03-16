class Solution:
    def isBalanced(self, s: str) -> bool:
        se=0
        so=0
        for i in range(len(s)):
            if(i%2==0):
                se+=int(s[i])
            else:
                so+=int(s[i])

        return se==so

        