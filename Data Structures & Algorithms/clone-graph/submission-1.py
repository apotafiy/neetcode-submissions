"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, entry: Optional['Node']) -> Optional['Node']:
        if not entry:
            return None
        visited = set()
        created = {}
        head = Node(entry.val, [])
        created[head.val] = head
        def dfs(node, node_):
            if node in visited:
                return
            for n in node.neighbors:
                if n.val in created:
                    node_.neighbors.append(created[n.val])
                else:
                    new = Node(n.val, [])
                    created[new.val] = new
                    node_.neighbors.append(new)
            visited.add(node)
            for i in range(len(node.neighbors)):
                dfs(node.neighbors[i], node_.neighbors[i])
            
        dfs(entry, head)

        return head