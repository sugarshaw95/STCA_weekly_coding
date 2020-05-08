class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import Counter
        array=[n%60 for n in time]
        #print(array)
        count=Counter(array)
        #maxx=max(time)
        res=0
        for t in count:
            if t==0 or t==30:
                res+=(count[t]-1)*count[t]
            else:
                res+=count[60-t]*count[t]
        return res//2