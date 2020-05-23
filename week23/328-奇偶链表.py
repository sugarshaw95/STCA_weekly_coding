class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head=None
        even_head=None
        before_odd=None
        before_even=None
        n=head
        count=1
        #奇链表和偶链表先分别建立,再把偶接在奇的后面
        while n:
            if count:
                if not odd_head:
                    odd_head=n
                else:
                    before_odd.next=n
                before_odd=n
                count=0
                
            else:
                if not even_head:
                    even_head=n
                else:
                    before_even.next=n
                before_even=n
                count=1
            n=n.next
        if before_odd:
            before_odd.next=even_head
        if before_even:
            before_even.next=None
        return odd_head