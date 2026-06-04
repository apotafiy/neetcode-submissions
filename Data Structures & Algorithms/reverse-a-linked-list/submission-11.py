# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        while head.next:
            next = head.next
            print(f"prev={None if not prev else prev.val},head={head.val},next={next.val}")
            head.next = prev
            prev = head
            head = next 
        head.next = prev
        return head