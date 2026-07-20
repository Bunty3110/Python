# 1022. Sum of Root To Leaf Binary Numbers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.

 

# Example 1:


# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def backtr(comb,CN):
            if CN.left is None and CN.right is None:
                ans.append(comb+str(CN.val))
                return
            comb+=str(CN.val)
            if CN.left is not None:
                backtr(comb,CN.left)
            if CN.right is not None:
                backtr(comb,CN.right)
        backtr("",root)
        total=0
        for i in ans:
            k=0
            num=0
            for j in range(len(i)-1,-1,-1):
                num+=int(i[j])* 2**k
                k+=1
            total+=num
        return total
