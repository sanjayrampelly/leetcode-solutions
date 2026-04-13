class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        count = 0

        for w in words:
            is_valid = True

            for ch in w:
                if ch in broken:
                    is_valid = False
                    break

            if is_valid:
                count += 1

        return count