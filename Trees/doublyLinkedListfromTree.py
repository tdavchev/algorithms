class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def bst_to_doubly(root):
    if root == None:
        return None

    stack = []
    prev = None
    ans = []

    while len(stack) != 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
            continue

        ans.append(stack[-1])
        root = stack[-1].right
        stack.pop()

    if len(ans) > 2:
        node = Node(ans[1].data)
        node.prev = Node(ans[0].data)
        node.next = Node(ans[2].data)

    ans.append(None)
    head = node.prev
    head.next = node
    curr = node.next
    curr.prev = node
    n = 3

    while curr != None and len(ans) > n:
        if curr.prev == None:
            curr.prev = prev

        if ans[n] != None:
            curr.next = Node(ans[n].data)
        prev = curr
        curr = curr.next
        n += 1

    return head


root = TreeNode(100)
ele1 = TreeNode(50)
ele2 = TreeNode(25)
ele3 = TreeNode(75)
ele4 = TreeNode(200)
ele5 = TreeNode(125)
ele6 = TreeNode(350)

root.set_left(ele1)
root.set_right(ele4)
ele1.set_left(ele2)
ele1.set_right(ele3)
ele4.set_left(ele5)
ele4.set_right(ele6)

ans = bst_to_doubly(root)

while ans != None:
    print("------")
    if ans.prev != None:
        print(ans.prev.data)
    else:
        print("None")
    # print(ans.prev.data)
    print(ans.data)
    if ans.next != None:
        print(ans.next.data)
    else:
        print("None")
    # print(ans.next.data)
    print("------")
    ans = ans.next
        