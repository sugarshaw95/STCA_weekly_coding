class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #对每个位置,要有next_smaller和before_smaller
        n=len(heights)
        next_smaller=[n for i in range(n)]
        before_smaller=[-1 for i in range(n)]
        ##单调减栈,top最大
        s=[]
        for i in range(n):
            #ii=-1
            while s and s[-1][1]>heights[i]:
                ii,hh=s.pop()
                next_smaller[ii]=i
            #before_smaller[i]=ii
            s.append((i,heights[i]))
            if len(s)>1:
                before_smaller[i]=s[-2][0]
        #print(before_smaller)
        #print(next_smaller)
        ret=0
        for i in range(n):
            ret=max(ret,heights[i]*(next_smaller[i]-before_smaller[i]-1))
        return ret