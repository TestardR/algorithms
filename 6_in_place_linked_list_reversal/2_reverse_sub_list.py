class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current # p - 1
        current = current.next # p
        i += 1
        
    last_node_of_first_part = previous
    # after reversing 'current' will become the last node of the sub-list
    last_node_sub_list = current
    next = None
    
    i = 0
    # reverse nodes 'p' and 'q'
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
        
    # connect with the first part
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous
    # in case of p == 1
    else: 
        head = previous
        
    last_node_sub_list.next = current

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    result.print_list()


main()
