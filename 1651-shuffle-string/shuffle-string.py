class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        cs = [0] * len(indices)
        
        for i in range(len(indices)):
            cs[indices[i]] = s[i]
        return "".join(cs)
