class Solution:
    def start_linkedlist_cycle(self, head):
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None

        while head != slow:
            head = head.next
            slow = slow.next


        return head