class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        
        hm={}

        for ch in s:
            if ch in hm:
                hm[ch]+=1
            else:
                hm[ch]=1
        
        for ch in t:
            if ch not in hm:
                return False
            hm[ch]-=1

            if hm[ch]<0:
                return False
        
        return True
