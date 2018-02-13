class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(head):
    curr = head
    length = 0
    while curr != None:
        length+=1
        curr = curr.next

    return length

def swap_nth_node(head, n):
    prev = None
    current = head

    if head == None:
        return head

    if n == 1:
        return head

    count = 1
    while current != None and count < n:
        prev = current
        current = current.next
        count += 1

    if current == None:
        return head

    prev.next = head
    temp = head.next
    head.next = current.next
    current.next = temp

    return current

def swap_n_repeat(head, n):
    if head == None:
        return head

    curr = head
    prev = None

    count = 0

    while curr != None and n-1 > count:
        prev = curr
        curr = curr.next
        count += 1

    if curr == None:
        return head.next

    prev.next = head
    temp = head.next
    head.next = curr.next
    curr.next = temp

    return curr

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

ans = swap_n_repeat(node1, 4)

while ans != None:
    print(ans.data)
    ans = ans.next