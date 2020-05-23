class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        before=None
        n=head
        while n:
            if before and  before.val==n.val:
                before.next=n.next
                #n=n.next
            else:
                before=n
                #n=n.next
            n=n.next
        return head