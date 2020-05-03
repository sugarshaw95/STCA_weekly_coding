class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        ret=set()
        l=10
        n=len(s)
        for b in range(n-l+1):
            substr=s[b:b+l]
            if substr in seen:
                ret.add(substr)
            else:
                seen.add(substr)
        return list(ret)