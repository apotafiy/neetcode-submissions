# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        k_ = 1
        def help(node: TreeNode, k: int) -> int:
            if not node:
                return -1
            l = help(node.left, k)
            nonlocal k_
            ret = node.val if k_ == k else -1
            k_ += 1
            return max(l, ret, help(node.right, k))
        return help(root, k)
            