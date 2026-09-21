class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}

        for i in range(len(nums)):
            hm[nums[i]]=i
        for i in range(len(nums)):
            x=target-nums[i]
            if x in hm and hm[x]!=i:
                return [i,hm[x]]
        
