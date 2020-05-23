class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        before=None
        n=head
        while n:
            if n.val==val:
                if before:
                    before.next=n.next
                else:
                    head=n.next
            before=n
            n=n.next
        return head