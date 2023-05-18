class Solution:
    def cycle_linkedlist(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
            
        return False
    

            