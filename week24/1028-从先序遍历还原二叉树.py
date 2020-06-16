# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if S=='':
            return None
        h=0
        num=''

        s_list=[]
        i=0
        while i<len(S):
            if S[i]=='-':
                s_list.append((int(num),h))
                num=''
                h=0                
                while S[i]=='-':
                    i+=1
                    h+=1


            else:
                num+=S[i]
                i+=1
        s_list.append((int(num),h))
        #print(s_list)
        def helper(s_list):
            root_v,root_h=s_list[0]
            root=TreeNode(root_v)
            if len(s_list)==1:
                return root
            kids=[]
            for i in range(len(s_list)):
                if s_list[i][1]==root_h+1:
                    kids.append(i)
            if not kids:
                return root
            if len(kids)==1:
                root.left=helper(s_list[kids[0]:])
                return root
            else:
                left=s_list[kids[0]:kids[1]]
                right=s_list[kids[1]:]
                #print(left,right)
                root.left=helper(left)
                root.right=helper(right)
                return root
        return helper(s_list)
