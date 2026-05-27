# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def help(node) -> bool:
            if not node:
                return True
            l = help(node.left)
            is_node_valid = True
            nonlocal prev
            if prev == None or prev < node.val:
                prev = node.val
            elif prev >= node.val:
                is_node_valid = False
            return l and is_node_valid and help(node.right)
        return help(root)
