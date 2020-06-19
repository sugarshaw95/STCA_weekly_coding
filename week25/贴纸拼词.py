from collections import Counter
from math import ceil
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def dominate(count_A,count_B):
            #count_A=Counter(count_A)
            #count_B=Counter(count_B)
            #return count_A&count_B==count_B

            if count_B.keys()-count_A.keys():
                return False
            for c in count_B:
                if count_B[c]>count_A[c]:
                    return False
            return True

            ##A dominate B?

        count_t=Counter(target)
        list_t=list(count_t.keys())
        ret=-1
        #print(count_t)

        ##得到candidates 只考虑target中的字符 并去掉覆盖的
        candidates=[]
        stickers.sort(key=lambda x:len([c for c in x if c in count_t]),reverse=True)
        ##按有效字符数排序 然后从最大的开始 这样可以保证有效去重
        for s in stickers:
            count_s=Counter(s)&count_t
            #count_s={key:count_s[key] for key in count_s.keys()& count_t.keys()}
            if count_s:
                skip=False
                for c in candidates:
                    if dominate(c,count_s):
                        skip=True
                        break
                if not skip:
                    candidates.append(count_s)
        
        candidates.sort(key=lambda x:len(x),reverse=True)
        ss=set()
        for c in candidates:
            ss=ss|c.keys()
        if ss!=count_t.keys():
            return ret
        ret=len(target)

        
        def backtrace(i,state,num):
            #print(state,num)
            nonlocal ret
            if num>ret:
                return
            '''
            tuple_state=tuple((k,state[k]) for k in list_t)
            if tuple_state not in dicc:
                dicc[tuple_state]=num
            elif dicc[tuple_state]<=num:
                return
            else:
                dicc[tuple_state]=num
            '''
            #剪枝似乎还慢了...    
            

            if dominate(state,count_t):
                #print(state,num)
                if num<ret:
                    ret=num
                return
            ##只选能增加不够的
            #need=[]
            #for c in count_t:
            #    if state[c]<count_t[c]:
            #        need.append(c)

            for ii in range(i,len(candidates)):
                count=candidates[ii]
                for c in count:
                    if state[c]<count_t[c]:
                        state+=count
                        backtrace(ii,state,num+1)
                        state-=count
                        break


        backtrace(0,Counter(),0)
        #print('count:',countt)

        return ret