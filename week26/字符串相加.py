class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret=''
        m=len(num1)
        n=len(num2)
        if m==0:
            return num2
        if n==0:
            return num1
        if m<n:
            num1,num2=num2,num1
            m,n=n,m
        jin=0
        for i in reversed(range(m)):
            x=int(num1[i])
            y=int(num2[i+(n-m)]) if i+(n-m)>=0 else 0
            wei=(x+y+jin)%10
            jin=(x+y+jin)//10
            #print(x,y,wei,jin)
            ret=str(wei)+ret

        if jin>0:
            ret=str(jin)+ret
        return ret 