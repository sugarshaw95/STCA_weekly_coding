class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        #ret=[]
        #nonlocal ret
        def check(s):
            return not (len(s)>1 and s[0]=='0') 
        def back(ii,tmp_arr):
            #if tmp_arr[:2]==[539834657,21]:
            #    print(ii,tmp_arr)
            #print(ii,tmp_arr)
            if ii==n:
                #print(ii,tmp_arr)
                return tmp_arr
            if len(tmp_arr)<2:
                return []
            else:
                if int(num[ii:])<tmp_arr[-1]+tmp_arr[-2]:
                    return []
                number=0
                for i in range(ii,n):
                    number=10*number+int(num[i])
                    if number==tmp_arr[-1]+tmp_arr[-2] and check(num[ii:i+1]):
                        rr=back(i+1,tmp_arr+[number])
                        if rr:
                            #print(tmp_arr+[num])
                            return rr

            return []

        for i in range(2,((2*n)//3)+1):
            for k in range(1,i):
                #print(i+1,[int(num[:k]),int(num[k:i+1])])
                if check(num[:k]) and check(num[k:i]):
                    
                    v=back(i,[int(num[:k]),int(num[k:i])])
                    if v:
                        return True
    



        return False