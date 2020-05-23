class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes=[]
        n=head
        while n:
            nodes.append(n)
            n=n.next
        l=len(nodes)
        before=None
        count=0
        i=0
        while count<l:
            x=nodes[i]
            #print(x.val)
            if count==l-1:
                x.next=None
            else:
                if i<l//2:
                    y=nodes[l-1-i]
                    i=l-1-i
                else:
                    y=nodes[l-1-i+1]
                    i=l-1-i+1
                #print(x.val,y.val)
                x.next=y
            count+=1