class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26

        for c in s:
            count[ord(c)-97]+=1
        
        for c in t:
            count[ord(c)-97]-=1
        
        for num in count:
            if num!=0:
                return False
        return True