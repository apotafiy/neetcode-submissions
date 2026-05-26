# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_list = self.getAncestors(root, p)
        print(list(map(lambda a: a.val, p_list)))
        q_list = self.getAncestors(root, q)
        print(list(map(lambda a: a.val, q_list)))
        p_end = len(p_list) - 1
        q_end = len(q_list) - 1
        while p_end >= 0 or q_end >= 0:
            print(p_end)
            print(q_end)
            if p_end < 0:
                return p_list[0]
            if q_end < 0:
                return q_list[0]
            if p_list[p_end] != q_list[q_end]:
                return p_list[p_end + 1]
            p_end -= 1
            q_end -= 1

    def getAncestors(self, root: TreeNode, target: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        if root.val == target.val:
            return [root]
        else:
            l = self.getAncestors(root.left, target)
            if len(l) > 0:
                l.append(root)
                return l
            r = self.getAncestors(root.right, target)
            if len(r) > 0:
                r.append(root)
                return r
            return []