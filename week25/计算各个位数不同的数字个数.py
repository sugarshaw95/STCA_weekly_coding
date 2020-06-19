class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n>10:
            return 0
        if n==0:
            return 1
        if n==1:
            return 10
        dp=[0 for i in range(n+1)]
        dp[1]=10
        dp[2]=81
        #def backtrace()
        ret=0
        for i in range(3,n+1):
            #print(helper(i))
            dp[i]=dp[i-1]*(11-i)
        return sum(dp)