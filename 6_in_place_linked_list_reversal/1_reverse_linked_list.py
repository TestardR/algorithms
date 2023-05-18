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
        
def reverse(head):
    previous, current, next = None, head, None
    while current is not None:
        next = current.next # tmp store next node
        current.next = previous # reverse current node
        previous = current # before we move to next node, point previous to current
        current = next # move to next node
        
    return previous


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    

    head.print_list()
    result = reverse(head)
    result.print_list()
    
main()