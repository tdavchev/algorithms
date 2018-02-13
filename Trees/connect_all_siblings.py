def populate_sibling_pointers(root):
    if root == None:
        return

    current = root
    last = root

    while current != None:
        if current.left != None:
            last.next = current.left
            last = current.left

        if current.right != None:
            last.next = current.right
            last = current.right

        last.next = None
        current = current.next


def populate_sibling_pointers_2(root):
    if root == None:
        return

    queue = deque()
    queue.append(root)
    prev = None

    while queue:
        temp = queue.popleft()

        if prev != None:
            prev.next = temp

        prev = temp

        if temp.left != None:
            queue.append(temp.left)

        if temp.right != None:
            queue.append(temp.right)

    prev.next = None