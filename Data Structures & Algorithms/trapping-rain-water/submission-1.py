class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1

        left_max=height[l]
        right_max=height[r]

        res=0

        while l<r:
            if left_max<right_max:
                l+=1
                left_max=max(left_max,height[l])
                water=left_max-height[l]
                res+=water
            else:
                r-=1
                right_max=max(right_max,height[r])
                water=right_max-height[r]
                res+=water
        return res