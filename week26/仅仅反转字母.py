class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ret=list(S)
        n=len(S)

        l=0
        r=n-1
        while l<r:
            if ret[l].isalpha() and ret[r].isalpha():
                ret[l],ret[r]=ret[r],ret[l]
                l+=1
                r-=1
            elif ret[l].isalpha() and not ret[r].isalpha():
                r-=1
            elif not ret[l].isalpha() and ret[r].isalpha():
                l+=1
            else:
                l+=1
                r-=1


        return ''.join(ret)