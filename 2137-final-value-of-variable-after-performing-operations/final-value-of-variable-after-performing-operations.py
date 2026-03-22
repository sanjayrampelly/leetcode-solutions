class Solution:
    def finalValueAfterOperations(self, a: List[str]) -> int:
        x = 0

        for e in a:
            if e == "X++" or e == "++X":
                x += 1
            else:
                x -= 1

        return x
