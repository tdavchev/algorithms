# Write a piece of code to determine whether
# a binary tree is a binary search tree or not

class Tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

    def delete(self, node, k):
        if node == None:
            return None
        elif node.data == k:
            if node.left is None and node.right is None:
                return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            node.data = get_min(node.right)
            node.right.delete(node.right, node.data)
        elif k < node.data:
            node.left.delete(node.left, k)
        else:
            node.right.delte(node.right, k)
        return node

def traverse(head):
    if head != None:
        is_bst(head.left)
        print(head.data)
        is_bst(head.right)

def iterative_traversal(root):
    if root == None:
        return

    stk = []
    while len(stk) != 0 or root != None:
        if root != None:
            stk.append(root)
            root = root.left
            continue

        print(stk[-1].data)
        root = stk.pop().right

def find_leftmost(root):
    prev = root
    while root != None:
        prev = root
        root = root.left
    
    return prev


def find_successor(root, data):
    if root == None:
        return

    stk = []
    prev = None
    while (len(stk) != 0 or root != None):
        if root != None:
            if root.data == data:
                if root.right == None:
                    while(len(stk) > 0):
                        if stk[-1].data < root.data:
                            stk.pop()
                        else:
                            print(stk[-1].data)
                            return
                    print("None")
                    return
                else:
                    print(find_leftmost(root.right).data)
                    return
            stk.append(root)
            root = root.left
            continue

        root = stk.pop().right

def is_bst(root):
    if root == None:
        return True

    if root.left != None:
        if root.data < root.left.data:
            return False
    
    if root.right != None:
        if root.data > root.right.data:
            return False

    return is_bst(root.left) & is_bst(root.right)

head = Tree(100)
node1 = Tree(50)
node2 = Tree(200)
node3 = Tree(25)
node4 = Tree(75)
node5 = Tree(125)
node6 = Tree(350)
head.set_left(node1)
head.set_right(node2)
node1.set_left(node3)
node1.set_right(node4)
node2.set_left(node5)
node2.set_right(node6)

# find_successor(head, 75)
print(is_bst(head))