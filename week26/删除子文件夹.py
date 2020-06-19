class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        lenn=0
        first=True
        ss=n-1
        while ss>=0 and s[ss]==' ':
            ss-=1  
        if ss==-1:
            return 0

        for i in range(ss,-1,-1):
            if s[i]==' ':

                return lenn
            else:
                lenn+=1
        return lenn