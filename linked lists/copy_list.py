class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbitrary = None

class pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def deep_copy_constant_space(head):
    if head == None:
        return None

    current = head

    while current != None:
        new_node = Node(current.data)

        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    current = head
    while current != None:
        if current.arbitrary != None:
            current.next.arbitrary = current.arbitrary.next

        current = current.next.next

    current = head
    new_head = head.next
    copied_current = new_head

    while current != None:
        copied_current = current.next
        current.next = copied_current.next
        
        if copied_current.next != None:
            copied_current.next = copied_current.next.next

        current = current.next

    return new_head

def deep_copy_constant_space(head):
    curr = head
    new_head = None
    new_current = None

    while curr != None:
        node = Node(curr.data)
        node.arbitrary = curr.arbitrary
            
        if new_head == None:
            new_head = node
            new_current = new_head
        else:
            new_current.next = node
            new_current = node

        # print_list(new_current)
        # dicto[curr.data] = node
        curr = curr.next


    new = new_head
    while new != None:
        if new.arbitrary != None:
            new.arbitrary = traverse(new_head, new.arbitrary.data)
        new = new.next

    # print_list(new_head)
    head.arbitrary = head.next
    print_list(new_head)
    print_list(head)

def traverse(head, data):
    curr = head
    while curr != None:
        if curr.data == data:
            return curr

        curr = curr.next

    return None


def deep_copy(head):
    curr = head
    new_head = None
    dicto = {}
    new_current = None

    while curr != None:
        node = Node(curr.data)
        node.arbitrary = curr.arbitrary
            
        if new_head == None:
            new_head = node
            new_current = new_head
        else:
            new_current.next = node
            new_current = node

        # print_list(new_current)
        dicto[curr.data] = node
        curr = curr.next

    upd = new_head
    while upd != None:
        if upd.arbitrary != None:
            upd.arbitrary = dicto[upd.arbitrary.data]
        upd = upd.next

    print_list(new_head)
    head.arbitrary = head.next
    print_list(head)

def print_list(head):
    curr = head
    while curr != None:
        if curr.arbitrary != None:
            print(curr.data, curr.arbitrary.data)
        else:
            print(curr.data, None)
        curr = curr.next

    print("finished---")



def copy(head):
    curr = head
    return curr

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node1.arbitrary = node4
node2.next = node3
node2.arbitrary = node1
node3.next = node4
node3.arbitrary = node5
node4.next = node5
node4.arbitrary = None
node5.arbitrary = node1
# node5.next = node6

deep_copy_constant_space(node1)