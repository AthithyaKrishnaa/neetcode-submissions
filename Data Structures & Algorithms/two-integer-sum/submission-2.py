class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}

        for i,val in enumerate(nums):
            x=target-val

            if x in hm:
                return [hm[x],i]

            hm[val]=i
