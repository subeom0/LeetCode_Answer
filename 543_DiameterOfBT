# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia: int = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.dia = max(self.dia, left + right + 2)
            
            return max(left, right) + 1
        dfs(root)
        return self.dia
