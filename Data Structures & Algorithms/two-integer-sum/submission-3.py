class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}

        for i in range(len(nums)):
            x=target-nums[i]

            if x in hm:
                return [hm[x],i]
            
            hm[nums[i]]=i
