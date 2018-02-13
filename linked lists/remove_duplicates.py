class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # the node initially pointes to None

def remove_duplicates(head):
    dup_set = set()

    dup_set.add(head.data)
    curr = head

    while cur.next != None:
        if cur.next.data in dup_set:
            cur.next = cur.next.next
        else:
            dup_set.add(cur.next.data)
            cur = cur.next

    return head