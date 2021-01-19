# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

# 5
# / \
# 4   8
# /   / \
# 11  13  4
# /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum_int: int) -> bool:
        if root == None:
            return False
        elif root.left == None and root.right == None and sum_int - root.val == 0:
            return True
        else:
            return hasPathSum(self, root.left, sum_int - root.val) or hasPathSum(
                self, root.right, sum_int - root.val
            )


class Solution:
    def hasPathSum(self, root: TreeNode, sum_int: int) -> bool:
        if root == None:
            return False
        sum_int -= root.val
        if root.left == None and root.right == None:
            return sum_int == 0
        left = self.hasPathSum(root.left, sum_int)
        right = self.hasPathSum(root.right, sum_int)
        return left or right


class Solution:
    def has_path_sum(self, root, sum_int):
        if root == None:
            return False
        sum_int -= root.val
        if root.left == None and root.right == None:
            return sum_int == 0
        left = self.has_path_sum(root.left, sum_int)
        right = self.has_path_sum(root.right, sum_int)
        return left or right
