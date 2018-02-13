class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def print_head(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def merge_lists(head1, head2):
    curr1 = head1
    curr2 = head2
    prev = None
    turns = 0
    while curr1 != None and curr2 != None:
        if curr1.data < curr2.data:
            if prev == None or turns == 1:
                turns = 1
                prev = curr1
                curr1 = curr1.next
            else:
                temp1 = curr2
                temp2 = curr1.next

                prev.next = curr1
                prev.next.next = temp1

                curr1 = temp2
        else:
            if prev == None or turns==2:
                turns = 2
                prev = curr2
                curr2 = curr2.next
            else:
                temp1 = curr1
                temp2 = curr2.next

                prev.next = curr2
                prev.next.next = temp1

                prev = curr2
                curr2 = temp2

    if turns == 1:
        return head1
    else:
        return head2

    return None

# less painful
def merge_sorted(head1, head2):
    if head1 == None:
        return head2
    elif head2 ==None:
        return head1

    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        if head1.data <= head2.data:
            mergedTail.next = head1
            mergedTail = head1
            head1 = head1.next
        else:
            mergedTail.next = head2
            mergedTail = head2
            head2 = head2.next

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    print_head(mergedHead)
    return mergedHead


node1 = Node(4)
node2 = Node(8)
node3 = Node(15)
node4 = Node(19)
node5 = Node(21)


node21 = Node(7)
node22 = Node(9)
node23 = Node(10)
node24 = Node(16)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node21.next = node22
node22.next = node23
node23.next = node24

ans = merge_sorted(node1, node21)
# while ans != None:
#     print(ans.data)
#     ans = ans.next
