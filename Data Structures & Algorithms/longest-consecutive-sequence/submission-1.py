class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        longest=0
        for num in nums:
            if num-1 not in nums_set:
                i=0
                while num+i in nums_set:
                    i+=1
                longest=max(longest,i)
        return longest
            
