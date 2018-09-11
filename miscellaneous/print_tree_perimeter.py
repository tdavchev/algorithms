class Tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def print_per(root):
    if root == None:
        return

    stk = []
    temp = root.right
    while root != None:
        print(root.data)
        stk.append(root)
        root = root.left

    while len(stk) != 0 or root != None:
        if root != None:
            if root.left == None and root.right == None:
                print(root.data)

            stk.append(root)
            root = root.left
            continue

        root = stk.pop().right


    while temp != None:
        if temp.right != None:
            print(temp.data)

        temp = temp.right

head = Tree(1)
node1 = Tree(2)
node2 = Tree(3)
node3 = Tree(4)
node4 = Tree(5)
node5 = Tree(7)
node6 = Tree(8)
node7 = Tree(9)
node8 = Tree(10)
head.set_left(node1)
head.set_right(node2)
node1.set_left(node3)
node1.set_right(node4)
node3.set_left(node7)
node4.set_right(node6)
node2.set_right(node5)
node5.set_right(node8)

print_per(head)