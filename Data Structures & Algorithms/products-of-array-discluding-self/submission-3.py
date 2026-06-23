class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        left=[]
        pr=1

        for i in range(n):
            left.append(pr)
            pr*=nums[i]

        right=[]
        pr=1

        for i in range(n-1,-1,-1):
            right.append(pr)
            pr*=nums[i]
        
        right=right[::-1]

        res=[]
        for i in range(n):
            res.append(left[i]*right[i])

        return res
