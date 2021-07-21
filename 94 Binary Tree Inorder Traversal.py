# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        val = []
        if not root:
            return []
        def inorderT(root):
            if root.left:
                inorderT(root.left)
            val.append(root.val)
            if root.right:
                inorderT(root.right)
            
        inorderT(root)
        return val
