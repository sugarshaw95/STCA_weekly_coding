class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix==[]:
            return 0
        m=len(matrix)
        n=len(matrix[0])


        #dp递推式和求全为1的最大正方形相同,dp[i][j]代表以i,j为右下角的最大正方形边长,最后把dp结果求和即可
        dp=[[0 for i in range(n)] for j in range(m)]
        max_t=0
        res=0
        dp[0][0]=1 if matrix[0][0]==1 else 0  
        #res+=dp[0][0]      
        for i in range(m):
            dp[i][0]=1 if matrix[i][0]==1 else 0 
            res+=dp[i][0] 

        for j in range(n):
            dp[0][j]=1 if matrix[0][j]==1 else 0
            res+=dp[0][j] 
        res-=dp[0][0]       

                
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res+=dp[i][j]
        

        return res