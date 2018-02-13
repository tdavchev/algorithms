class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_alternating(head, list_even):
    curr = head
    currHead = head
    currTail = head
    curr = curr.next
    while curr != None:
        currTail.next = list_even
        currTail = list_even

        currTail.next = curr
        currTail = curr

        list_even = list_even.next
        curr = curr.next

    if list_even != None:
        currTail.next = list_even
        currTail = list_even

    return currHead
        
def reverse_even(head):
    curr = head
    list_even = None

    while curr != None and curr.next != None:
        even = curr.next
        curr.next = even.next

        even.next = list_even
        list_even = even

        curr = curr.next

    return merge_alternating(head, list_even)

def print_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

    print("finished---")

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)
# node6 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6

ans = reverse_even(node1)
print("tuk sam")
while ans != None:
    print(ans.data)
    ans = ans.next