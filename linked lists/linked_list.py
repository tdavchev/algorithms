class Node:
    def __init__(self, value):
        self.val = val
        self.next = None # the node initially pointes to None
        

def reverse_recursive(head):
    if head == None or head.next == None:
        return head

    reversed_list = reverse_recursive(head.next)
    
    head.next.next = head
    head.next = None

    return reversed_list