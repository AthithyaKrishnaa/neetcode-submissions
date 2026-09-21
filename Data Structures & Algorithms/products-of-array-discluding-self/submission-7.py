class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l=[]
        pr=1
        for i in range(len(nums)):
            l.append(pr)
            pr*=nums[i]
        
        r=[]
        pr=1
        for i in range(len(nums)-1,-1,-1):
            r.append(pr)
            pr*=nums[i]
        r=r[::-1]
        
        res=[]
        for i in range(len(nums)):
            res.append(l[i]*r[i])
        return res
