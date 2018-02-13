class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def add_them(head1, head2):
    curr1 = head1
    curr2 = head2
    carry = 0
    
    result = curr1.data + curr2.data + carry
    if result > 9:
        carry = 1
        result = result % 10
    
    head_node = Node(result)
    result_tail = head_node
    result_head = head_node
    curr1 = curr1.next
    curr2 = curr2.next
    while curr1 != None or curr2 != None:
        if curr1 == None:
            curr1_data = 0
            curr2 = curr2.next
        elif curr2 == None:
            curr2_data = 0
            curr1 = curr1.next
        else:
            curr1_data = curr1.data
            curr2_data = curr2.data
            curr1 = curr1.next
            curr2 = curr2.next

        result = curr1_data + curr2_data + carry
        carry = 0
        if result > 9:
            carry = 1
            result = result % 10

        node = Node(result)
        result_tail.next = node
        result_tail = node


    if carry == 1:
        result_tail.next = Node(carry)

    return result_head



#8-3-1-0-1
node1 = Node(1)
node2 = Node(0)
node3 = Node(9)
node4 = Node(9)

node21 = Node(7)
node22 = Node(3)
node23 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

node21.next = node22
node22.next = node23

ans = add_them(node1, node21)
while ans != None:
    print(ans.data)
    ans = ans.next