class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[0 for i in range(n)]
        dp[0]=nums[0]
        dp[1]=nums[1]
        maxx=dp[0]
        for i in range(2,n):
            maxx=dp[i-2] if dp[i-2]>maxx else maxx
            dp[i]=maxx+nums[i]
        #print(dp)
        return max(dp)