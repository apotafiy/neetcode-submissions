# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def toList(node):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    return list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        print(f"Original List: {toList(head)}")
        if not head or not head.next:
            return
        list_size = 0
        node = head
        while node:
            node = node.next
            list_size += 1
        middle = (list_size + 1) // 2
        i = 0
        node = head
        while i < middle:
            node = node.next
            i += 1

        tail = self.reverseList(node)
        node = head
        i = 0
        while i < middle - 1:
            node = node.next
            i += 1
        node.next = None
        print(f"New Head: {toList(head)}")
        print(f"New Tail: {toList(tail)}")

        flag = True
        head_next = head.next
        tail_next = tail.next
        while head and tail:
            if flag:
                print(f"flag={flag},head={head.val},head_next={None if not head_next else head_next.val}")
                head.next = tail
                head = head_next
                if head:
                    head_next = head.next
            else:
                print(f"flag={flag},tail={tail.val},tail_next={None if not tail_next else tail_next.val}")
                tail.next = head
                tail = tail_next
                if tail:
                    tail_next = tail.next
            flag = not flag

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        while head.next:
            next = head.next
            print(
                f"prev={None if not prev else prev.val},head={head.val},next={next.val}"
            )
            head.next = prev
            prev = head
            head = next
        head.next = prev
        return head


