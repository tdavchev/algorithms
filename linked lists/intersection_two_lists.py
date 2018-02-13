class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def is_intersect(head1, head2):
    curr1 = head1

    while curr1 != None:
        curr2 = head2
        while curr2 != None:
            if curr1.data == curr2.data:
                return curr1.data
            curr2 = curr2.next
        curr1 = curr1.next

    return None

def intersect_quick(head1, head2):
    length1 = get_length(head1)
    length2 = get_length(head2)
    diff = abs(length1 - length2)
    if length1 > length2:
        curr_big = head1
        curr_small = head2
    else:
        curr_big = head2
        curr_small = head1

    for i in range(diff):
        curr_big = curr_big.next

    while curr_big != None:
        if curr_big.data == curr_small.data:
            return curr_big.data

        curr_big = curr_big.next
        curr_small = curr_small.next

    return None

def get_length(head):
    curr = head
    length = 0
    while curr != None:
        curr = curr.next
        length += 1

    return length

node1 = Node(29)
node2 = Node(23)
node3 = Node(82)
node4 = Node(11)
node5 = Node(12)
node6 = Node(27)

node21 = Node(13)
node22 = Node(4)
node23 = Node(12)
node24 = Node(27)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node21.next = node22
node22.next = node23
node23.next = node24

ans = intersect_quick(node1, node21)
print(ans)