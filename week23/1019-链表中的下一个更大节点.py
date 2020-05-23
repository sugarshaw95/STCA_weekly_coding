class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        s=[]
        ret=[]
        n=head
        i=0
        ##单调栈
        while n:
            ret.append(0)
            while s and s[-1][1]<n.val:
                ii,_=s.pop()
                #print(ii,_)
                ret[ii]=n.val
            s.append((i,n.val))            
            n=n.next
            i+=1
        return ret