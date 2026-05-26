# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        tail = head
         
        p1 = list1
        p2 = list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
                tail = tail.next
            else:
                tail.next = p2
                p2 = p2.next
                tail = tail.next
        if not p1:
            tail.next = p2
        else:
            tail.next = p1
        return head