class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k_nodes(head, k):
    if k <=1 or head == None:
        return head

    reversed = None
    prev_tail = None

    while head != None and k > 0:
        current_head = None
        current_tail = head

        n = k
        while head != None and n > 0:
            temp = head.next
            head.next = current_head
            current_head = head

            head = temp
            n -= 1

        if reversed == None:
            reversed = current_head

        if prev_tail != None:
            prev_tail.next = current_head

        prev_tail = current_tail

    return reversed

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

reverse_k(node1, 3)

# ans = rotate_linked_list(node1, 2)
# print("ANSWER:")
# while ans != None:
#     print(ans.data)
#     ans = ans.next