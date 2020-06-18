class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret=[]
        #appeared=set()
        
        def dfs(num,s,summ):
            #print(s,summ)
            nonlocal ret
            if len(s)==k:
                if tuple((s)) not in ret and summ==n:
                    ret.append(tuple(s))
                return
            for nn in range(num+1,10):
                ##按顺序 只考虑大于num的数 自动避免重复
                if nn not in s and summ+nn<=n:
                    
                    dfs(nn,s+[nn],summ+nn)
        dfs(0,[],0)
        return ret
