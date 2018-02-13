class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def nth_from_last(head, n):
    length = get_length(head)
    nth = length - n
    if nth < 0:
        return None

    count = 0

    while head != None:
        if count == nth:
            return head
        
        count += 1
        head = head.next

def get_length(head):
    curr = head
    length = 0
    while curr != None:
        length += 1
        curr = curr.next

    return length
    
node1 = Node(7)
node2 = Node(14)
node3 = Node(21)
node4 = Node(28)
node5 = Node(35)
node6 = Node(42)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ans = nth_from_last(node1, 3)
print(ans.data)
