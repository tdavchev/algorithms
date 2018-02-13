class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def rotate_linked_list(head, n):

    if head == None or head.next == None:
        return head

    length = get_length(head)
    n = n % length
    if n < 0:
        n += length

    rotate = length - n - 1

    temp = head

    count = 0
    for i in range(rotate):
        temp = temp.next

    new_head = temp.next
    temp.next = None

    temp = new_head
    
    while temp.next != None:
        temp = temp.next

    temp.next = head

    return new_head

def print_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

    print("finished---")
        

def get_length(head):
    curr = head
    length = 0
    while curr != None:
        length += 1
        curr = curr.next

    return length

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6

# rotate_linked_list(node1, 3)

ans = rotate_linked_list(node1, 2)
print("ANSWER:")
while ans != None:
    print(ans.data)
    ans = ans.next
