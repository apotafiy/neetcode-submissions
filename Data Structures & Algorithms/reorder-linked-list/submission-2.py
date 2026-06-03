# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        l = 0
        r = len(nodes) - 1
        print(list(node.val for node in nodes))
        flag = True
        while l < r:
            left = nodes[l]
            right = nodes[r]
            print(f"l = {l}, val = {left.val}")
            print(f"r = {r}, val = {right.val}")
            if flag:
                left.next = right
                l += 1
                if l == r:
                    nodes[r].next = None
            else:
                right.next = left
                r -= 1
                if l == r:
                    nodes[l].next = None
            flag = not flag
            