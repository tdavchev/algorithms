class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, key):
    current = head
    prev = None

    if current == None or current.next == None:
        return current

    while current != None:
        if current.data == key:
            break

        prev = current
        current = current.next

    if current == None:
        return head

    if current == head:
        return head.next

    prev.next = current.next

    return head

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

ans = delete_node(node1, 7)
print("ANSWER:")
while ans != None:
    print(ans.data)
    ans = ans.next