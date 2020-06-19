class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        qipan=[['.' for j in range(n)] for i in range(n)]
        #print(qipan)
        ret=[]
        def check(qipan,i,j):
            for ii in range(n):
                if ii==i:
                    continue
                if qipan[ii][j]=='Q':
                    return False
            #对角线
            for ii in range(i+j+1):
                jj=i+j-ii
                if ii<n and jj<n:
                    if ii==i:
                        continue
                    if qipan[ii][jj]=='Q':
                        return False
            for ii in range(0,n):
                jj=ii+(j-i)
                if 0<=jj<n:
                    if qipan[ii][jj]=='Q':
                        return False
            return True
        def backtrace(i,qipan):
            nonlocal ret
            if i==n:
                ret.append([''.join(l) for l in qipan])
            for j in range(n):
                if check(qipan,i,j):
                    qipan[i][j]='Q'
                    backtrace(i+1,qipan)
                    qipan[i][j]='.'
        backtrace(0,qipan)

        return ret