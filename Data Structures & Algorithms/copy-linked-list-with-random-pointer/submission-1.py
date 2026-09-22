"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        indices = {}
        ptr = head
        copied_arr = []
        i = 0
        while ptr:
            # track indices of og nodes
            indices[ptr] = i
            # create copy of list without randoms
            copied_arr.append(Node(ptr.val, None, None))
            if i != 0:
                copied_arr[i - 1].next = copied_arr[i]
            i += 1
            ptr = ptr.next
        
        ptr = head
        i = 0
        while ptr:
            if ptr.random:
                j = indices[ptr.random]
                copied_arr[i].random = copied_arr[j]
            i += 1
            ptr = ptr.next
        
        return copied_arr[0]