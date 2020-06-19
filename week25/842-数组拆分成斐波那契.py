class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n=len(S)
        ret=[]
        #nonlocal ret
        def check(s):
            return not (len(s)>1 and s[0]=='0') and (0<=int(s)<2**31-1)
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
                if int(S[ii:])<tmp_arr[-1]+tmp_arr[-2]:
                    return []
                #num=0
                for i in range(ii,n):
                    num=int(S[ii:i+1])
                    if num==tmp_arr[-1]+tmp_arr[-2] and check(S[ii:i+1]):
                        rr=back(i+1,tmp_arr+[num])
                        if rr:
                            #print(tmp_arr+[num])
                            return rr

            return []

        for i in range(2,((2*n)//3)+1):
            for k in range(1,i):
                #print(i+1,[int(S[:k]),int(S[k:i+1])])
                #探寻所有可能的前两个数
                if check(S[:k]) and check(S[k:i]):
                    
                    v=back(i,[int(S[:k]),int(S[k:i])])
                    if v:
                        return v
    



        return ret