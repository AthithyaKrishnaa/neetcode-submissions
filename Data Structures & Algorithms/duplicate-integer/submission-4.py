class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num in nums:
            if count[num]>1:
                return True
        return False

        