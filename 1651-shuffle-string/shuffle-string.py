class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        cs = [""] * len(indices)

        for i in range(len(indices)):
            cs[indices[i]] = s[i]
        return "".join(cs)
