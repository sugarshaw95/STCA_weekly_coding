class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        dp1=[0 for i in range(n+1)]
        # 不偷最后一家
        dp2=[0 for i in range(n+1)]
        # 不偷第一家
        dp1[1]=nums[0]
        for i in range(2,n+1):
            if i!=n:
                dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i-1])
            else:
                dp1[i]=max(dp1[i-1],dp2[i-2]+nums[i-1])
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i-1])
        #print(dp1[1:],dp2[1:])
        return dp1[-1]