class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n=node.next
        node.next=n.next
        #删掉next再把node变成node.next
        node.val=n.val