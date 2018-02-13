class Node:
    def __init__(self, val):
        self.val = val
        self.next = None # the node initially pointes to None

def reverse_singly(head):
    if (head == None) or (head.next == None):
        return head

    list_left = head.next
    reversed_list = head
    reversed_list.next = None

    while (list_left != None):
        temp = list_left
        list_left = list_left.next

        temp.next = reversed_list
        reversed_list = temp

    return reversed_list

def reverse_recursive(head):
    if head == None or head.next == None:
        return head

    # at the end head.next = 37
    # head is 99
    reversed_list = reverse_recursive(head.next)

    head.next.next = head
    head.next = None

    return reversed_list

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

ans = reverse_recursive(node1)
print("ANSWER:")
print(ans.val)