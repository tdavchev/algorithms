class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def sort_list(head, node):
    if node == None:
        return head

    if head == None or node.data <= head.data:
        node.next = head
        return node

    curr = head
    while curr.next != None and node.data > curr.next.data:
        curr = curr.next

    node.next = curr.next
    curr.next = node

    return head

def insertion_sort(head):
    if head == None or head.next == None:
        return head

    curr = head
    sorted_list = None

    while curr != None:
        temp = curr.next
        sorted_list = sort_list(sorted_list, curr)
        curr = temp

    return sorted_list


node1 = Node(29)
node2 = Node(23)
node3 = Node(82)
node4 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4

ans = insertion_sort(node1)
print("ANSWER:")
while ans != None:
    print(ans.data)
    ans = ans.next