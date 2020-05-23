class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        x=head
        x_before=None
        while x and x.next:
            y=x.next
            next_x=y.next
            #print(x.val,y.val)
            if x==head:
                head=y
            else:
                x_before.next=y                
            x.next=y.next
            y.next=x
            x_before=x
            x=next_x
            
        return head