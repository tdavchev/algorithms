# def merge_sort(head):
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def split_in_half(head, first_second):

    if head == None:
        first_second.first = None
        first_second.second = None
        return

    if head.next == None:
        first_second.first = head
        first_second.second = None
    else:
        slow = head
        fast = head.next

        while fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
                slow = slow.next

        first_second.first = head
        first_second.second = slow.next

        slow.next = None


def merge_sorted(head1, head2):
    if head1 == None:
        return head2

    if head2 == None:
        return head1

    sortedHead = None
    sortedTail = None
    if head1.data <= head2.data:
        sortedHead = head1
        sortedTail = head1
        head1 = head1.next
    else:
        sortedHead = head2
        sortedTail = head2
        head2 = head2.next

    while head1 != None and head2 != None:
        if head1.data <= head2.data:
            sortedTail.next = head1
            sortedTail = head1
            head1 = head1.next

        elif head2.data <= head1.data:
            sortedTail.next = head2
            sortedTail = head2
            head2 = head2.next

    if head1 != None:
        sortedTail.next = head1
    elif head2 != None:
        sortedTail.next = head2

    return sortedHead

def merge_sort(head):
    if head == None or head.next == None:
        return head

    first_second = pair(None, None)

    split_in_half(head, first_second)

    first_second.first = merge_sort(first_second.first)
    first_second.second = merge_sort(first_second.second)

    return merge_sorted(first_second.first, first_second.second)

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)
node21 = Node(2)
node22 = Node(4)
node23 = Node(6)
node24 = Node(8)
node25 = Node(10)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node21
node21.next = node22
node22.next = node23
node23.next = node24
node24.next = node25

ans = merge_sort(node1)
while ans != None:
    print(ans.data)
    ans = ans.next