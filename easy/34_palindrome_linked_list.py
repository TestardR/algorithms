# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        endOfFirstHalf = self.getEndOfFirstHalf(head) 
        p1 = head
        p2 = self.reverse(endOfFirstHalf)

        while p2:
            if p1.val != p2.val: return False

            p1 = p1.next
            p2 = p2.next

        return True

    def getEndOfFirstHalf(self, head):
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse(self, head):
        tail = head
        prev = None

        while tail:
            tmp = tail.next
            tail.next = prev
            prev = tail
            tail = tmp

        return prev

