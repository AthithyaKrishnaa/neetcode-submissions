class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count={}

        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        
        for ch in t:
            if ch not in count:
                return False
            count[ch]-=1
            if count[ch]<0:
                return False
        
        return True