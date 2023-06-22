class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev