# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        ender = head
        for i in range(n):
            ender = ender.next
        prev = None
        curr = head
        while ender:
            prev = curr
            curr = curr.next
            ender = ender.next
        if not prev:
            return curr.next
        elif not curr.next:
            prev.next = None
        else:
            prev.next = curr.next
        return head