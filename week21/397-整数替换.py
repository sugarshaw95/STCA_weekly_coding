class Solution:
    def integerReplacement(self, n: int) -> int:
        '''
        def helper(n):
            if n==1:
                return 0
            if n&1==0:
                return 1+helper(n>>1)
            else:
                return 1+min(helper(n+1),helper(n-1))

        return helper(n)
        '''

        ret=0
        while n>1:
            if (n&1)==0: # 偶数直接右移
                n>>=1
            else:
                n+= -1 if (n&2)==0 or n==3 else 1  # 奇数01或者3减一，其他加1 思想:尽量保留少的1,最后两位是11就+1,01就减1
            ret+=1
        return ret