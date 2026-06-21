class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        pr=1
        for num in nums:
            left.append(pr)
            pr*=num

        pr=1
        for i in range(len(nums)-1,-1,-1):
            right.append(pr)
            pr*=nums[i]
        right=right[::-1]

        res=[]
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res
            