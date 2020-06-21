from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        answers=[]
        counts=[]
        n=len(s)
        for i in range(n+1):
            counts.append(Counter(s[:i]))
        for l,r,k in queries:
            #l,r,k=q
            if k>13:
                answers.append(True)
                continue
            #sub_str=s[l:r+1]
            count=dict(counts[r+1]-counts[l])
            #count=dict(Counter(sub_str))
            odds=0
            for c in count:
                if count[c]%2:
                    odds+=1
            if odds-k*2>1:
                answers.append(False)
            else:
                answers.append(True)
        return answers
		##Python不位运算就超时...