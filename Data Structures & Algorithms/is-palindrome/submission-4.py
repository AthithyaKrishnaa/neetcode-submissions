class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=[]
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i])
        
        l,r=0,len(res)-1

        while l<r:
            if res[l]!=res[r]:
                return False
            l+=1
            r-=1
        return True