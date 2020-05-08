class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n=len(A)
        ret=[False for i in range(n)]
        summ=0
        for i in range(n):
            summ=summ*2+A[i]
            if summ>=10:
                summ=summ%10
            #只取个位即可(防溢出)
            #print(summ)
            if summ==0 or summ==5:
                ret[i]=True            
            
        return ret
