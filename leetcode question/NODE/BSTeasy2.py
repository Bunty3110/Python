# 94. Binary Tree Inorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def traverse(CN):
            if CN is None:
                return
            traverse(CN.left)
            result.append(CN.val)
            traverse(CN.right)
        traverse(root)
        return result