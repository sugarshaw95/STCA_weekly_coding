from collections import Counter
class Solution:
    def permutation(self, S: str) -> List[str]:
        if S=='':
            return ['']
        ret=[]
        n=len(S)
        set_s=set(S)
        count=Counter(S)
        #used=set()
        def dfs(count,ss):
            #print(count)
            #print(ss)
            nonlocal ret
            #nonlocal used
            if len(ss)==n:
                ret.append(ss)
                return
            for c in set_s:
                if count[c]>=1:
                    new_count=count.copy()
                    new_count[c]-=1
                    dfs(new_count,ss+c)
        dfs(count,'')
        return ret
