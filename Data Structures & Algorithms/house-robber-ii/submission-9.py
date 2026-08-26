class Solution:
    def rob(self, nums: List[int]) -> int:
        m=len(nums)
        if(m==1):
            return nums[0]
        def rob_case(arr):
            n=len(arr)
            if n==1:
                return arr[0]
            dp=[0]*n
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])

            for i in range(2,n):
                dp[i]=max(dp[i-1],arr[i]+dp[i-2])

            return dp[n-1]
        case1=rob_case(nums[1:])
        case2=rob_case(nums[:-1])

        return max(case1,case2)