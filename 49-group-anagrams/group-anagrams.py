class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            # print(key)
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())
