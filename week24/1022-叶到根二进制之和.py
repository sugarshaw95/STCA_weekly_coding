# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ret=0
        if not root:
            return 0
        s=[(root,str(root.val))]

        while s:
            n,num=s.pop(0)
            if not n.left and not n.right:
                ret+=int('0b'+num,2)
            if n.left:
                s.append((n.left,num+str(n.left.val)))
            if n.right:
                s.append((n.right,num+str(n.right.val)))
        return ret
