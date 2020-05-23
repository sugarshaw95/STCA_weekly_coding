class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ##相交的话,A'(A独有)+AB(AB共有)+B'(B独有)=B'+AB+A' 不相交就会走完A+B也没遇到 直接返回False
        na=headA
        nb=headB
        second_end_a=False
        second_end_b=False
        while na and nb:
            #print(na.val,nb.val)
            if na==nb:
                return na
            if na.next:
                na=na.next
            elif not second_end_a:
                na=headB
                second_end_a=True
            else:
                return None
            if nb.next:
                nb=nb.next
            elif not second_end_b:
                nb=headA
                second_end_b=True
            else:
                return None