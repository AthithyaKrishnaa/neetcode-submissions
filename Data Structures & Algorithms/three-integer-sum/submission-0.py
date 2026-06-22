class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]

        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=len(nums)-1

            while left<right:
                summ=nums[i]+nums[left]+nums[right]

                if summ==0:
                    answer.append([nums[i],nums[left],nums[right]])                 
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                
                elif summ<0:
                    left+=1
                else:
                    right-=1
        return answer