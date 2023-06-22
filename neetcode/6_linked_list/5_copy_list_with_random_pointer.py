"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None} # in case pointers are pointing to null

        # copy into hashmap
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
            
        # copy into 
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next] # if cur.next points to null, we initialize oldCopy with null values
            copy.random = oldToCopy[cur.random] # if cur.random points to null, we initialize oldCopy with null values
            cur = cur.next
            
        return oldToCopy[head]