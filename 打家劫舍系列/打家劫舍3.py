# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        #ret=0
        def dfs(root):

            if not root:
                return (0,0)

            left_use=0
            left_not=0
            right_use=0
            right_not=0           
            if root.left:
                left_use,left_not=dfs(root.left)
            if root.right:
                right_use,right_not=dfs(root.right)

            return (left_not+right_not+root.val,max(left_not,left_use)+max(right_not,right_use))
        ##dfs返回值: 以root为起点的最高金额 [0]是用了root的 1是没用root的
            
        #dfs(root,[])
        return max(dfs(root))