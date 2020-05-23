class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
	##不用额外空间，先快慢指针找相遇点，再用相遇点找环的入口
        n1=head
        n2=head
        met=False
        while n1 and n2:
            #print(n1.val,n2.val)
            if n1==n2:
                if not met:
                    met=True
                else:
                    #找到相遇点 二阶段 找入口 需要理解一下
                    s=head
                    while s!=n1:
                        s=s.next
                        n1=n1.next
                    return n1
            if not n1.next:
                return None
            if not n2.next or not n2.next.next:
                return None
            n1=n1.next
            n2=n2.next.next