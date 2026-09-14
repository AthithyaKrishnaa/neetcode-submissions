class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set=set(nums)
        longest=0
        
        for num in nums:
            if num-1 not in num_set:
                i=0
                while num+i in num_set:
                    i+=1
                longest=max(longest,i)
        return longest
        