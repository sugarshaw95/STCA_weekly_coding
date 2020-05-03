from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def judge(w1,w2):
            bitmask1=0
            bitmask2=0
            for c in w1:
                i=ord(c)-ord('a')
                bit=1<<i
                bitmask1=bit|bitmask1
            for c in w2:
                i=ord(c)-ord('a')
                bit=1<<i
                bitmask2=bit|bitmask2
            return bitmask1&bitmask2==0            
        def cal_bitmask(w):
            bitmask=0
            for c in w:
                i=ord(c)-ord('a')
                bit=1<<i
                bitmask=bit|bitmask
            return bitmask
        
        hashmap=defaultdict(int)
        for w in set(words):
            bitmask=cal_bitmask(w)
            hashmap[bitmask]=max(len(w),hashmap[bitmask])            

        ret=0
        for m in hashmap:
            for n in hashmap:
                if m&n==0:
                    ret=max(ret,hashmap[m]*hashmap[n])
        return ret