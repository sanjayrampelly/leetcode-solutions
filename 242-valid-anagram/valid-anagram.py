class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d1={}
        d2={}

        for ch in s:
            d1[ch]=d1.get(ch,0)+1
        
        for ch in t:
            d2[ch]=d2.get(ch,0)+1

        for k,v in d1.items():
            if k not in d2 or d2[k]!=v:
                return False

        return True
        