class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n=len(tiles)
        if n<=1:
            return n
        used=[False for i in range(n)]
        res=0
        appeared=set()
        def back_dfs(s,used):
            nonlocal res
            nonlocal appeared
            if s not in appeared:
                #print(s)
                res+=1
                appeared.add(s)
            if len(s)==n:
                return
            for i in range(n):
                if not used[i]:
                    used[i]=True
                    back_dfs(s+tiles[i],used)
                    used[i]=False
        back_dfs('',used)
        res-=1
        return res