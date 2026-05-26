# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.help(root, root.val)
    
    def help(self, root, max_) -> int:
        if not root:
            return 0
        max_ = max(max_, root.val)
        l = self.help(root.left, max_)
        r = self.help(root.right, max_)
        curr = 1 if max_ <= root.val else 0
        return curr + l + r