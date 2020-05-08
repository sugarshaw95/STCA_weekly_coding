class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        summ=sum(A)
        if summ%3:
            return False
        target=int(summ/3)
        #print('sum:',summ,'target:',target)
        i=0
        summ1=0
        while i<len(A)-2:
            summ1+=A[i]
            if summ1==target:
                break
            i+=1
        j=i+1
        summ2=0
        while j<len(A)-1:
            summ2+=A[j]
            if summ2==target:
                print(A[:i+1],A[i+1:j+1],A[j+1:])
                return True
            j+=1
        return False
