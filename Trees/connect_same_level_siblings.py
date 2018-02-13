class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def connect_next_level(head):
    current = head
    print("head is ", head.data)
    next_level_head = None
    prev = None

    while current != None:
        if current.left != None and current.right != None:
            print("ima i left i right")
            if next_level_head == None:
                next_level_head = current.left

            current.left.next = current.right

            if prev != None:
                prev.next = current.left

            prev = current.right
        elif current.left != None:
            print("ima samo left")
            if next_level_head == None:
                next_level_head = current.left

            if prev != None:
                prev.next = current.left

            if prev != None:
                prev.next = current.left

            prev = current.left
        elif current.right != None:
            print("ima samo right")
            if next_level_head == None:
                next_level_head = current.right

            if prev != None:
                prev.next = current.right

            prev = current.right

        current = current.next

    if prev != None:
        prev.next = None

    return next_level_head

def populate_sibling_pointers(root):
    if root == None:
        return

    root.next = None

    while root != None:
        root = connect_next_level(root)
        cur = root
        while cur != None:
            if cur.data != None:
                print(cur.data)
            else:
                print("None")
            cur = cur.next
        
        print("---")


root = TreeNode(100)
ele1 = TreeNode(50)
ele2 = TreeNode(25)
ele3 = TreeNode(75)
ele4 = TreeNode(10)
ele5 = TreeNode(15)
ele6 = TreeNode(200)
ele7 = TreeNode(300)
ele8 = TreeNode(350)


root.set_left(ele1)
root.set_right(ele6)
ele1.set_left(ele2)
ele1.set_right(ele3)
ele2.set_left(ele4)
ele4.set_right(ele5)
ele6.set_right(ele7)
ele7.set_right(ele8)

populate_sibling_pointers(root)