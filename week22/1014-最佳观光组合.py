class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        #A.sort()
        #for d in range(1,)
        n=len(A)
        if n<=1:
            return 0
        maxx=-n
        ret=0
        for i in reversed(range(n-1)):
            #保存从i+1开始到末尾的max(A[j]-j)
            #对每个位置i,只要算A[i]+i+max(A[j]-j)
            maxx=max(maxx,A[i+1]-(i+1))
            #print(maxx)
            ret=max(ret,A[i]+i+maxx)
        return ret