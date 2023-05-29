# O(N) T | O(1) S
def removeNthNodeFromEnd(head, n):
    counter = 1
    first = head
    second = head
    while counter <= n:
        second = second.next
        counter += 1
        
    # edge case
    if second is None:
        head = head.next
        return
    
    while second.next is not None:
        second = second.next
        first = first.next
        
    first.next = first.next.next
    
    
        