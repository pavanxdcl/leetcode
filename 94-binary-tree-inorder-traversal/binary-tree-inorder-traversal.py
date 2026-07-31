# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,s,root):
        if(root==None):
            return 
        self.traverse(s,root.left)
        s.append(root.val)
        self.traverse(s,root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s=[]
        self.traverse(s,root)
        return s