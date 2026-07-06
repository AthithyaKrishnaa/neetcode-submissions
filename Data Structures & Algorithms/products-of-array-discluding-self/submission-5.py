class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pr=1
        left=[]
        for num in nums:
            left.append(pr)
            pr*=num

        pr=1
        right=[]
        for i in range(n-1,-1,-1):
            right.append(pr)
            pr*=nums[i]
        right=right[::-1]
        
        res=[]
        for i in range(n):
            res.append(left[i]*right[i])
        return res