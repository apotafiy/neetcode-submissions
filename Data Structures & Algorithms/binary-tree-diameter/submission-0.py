# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)[1]

    def depth(self, root: Optional[TreeNode]):
        # return (deepest_child, max_d)
        if not root:
            return (0, 0)
        left_val = self.depth(root.left)
        right_val = self.depth(root.right)
        left_depth = left_val[0]
        right_depth = right_val[0]
        curr_d = left_depth + right_depth
        max_d = max(curr_d, left_val[1], right_val[1])

        max_depth = max(left_depth, right_depth) + 1
        return (max_depth, max_d)
