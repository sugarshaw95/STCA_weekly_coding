class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ret=0
        n=head
        G=set(G)
        ##有坑 这里链表没有重复元素 不然例如[0,1,0,1,3] G=[0,1,3] 应为1,这样贪心就会为2,无法保证最长
        while n:
            if n.val in G:
                l=[]
                #G.remove(n.val)
                while n and n.val in G:
                    G.remove(n.val)
                    l.append(n.val)
                    n=n.next
                #print(l)
                ret+=1
            else:
                n=n.next
        
        return ret