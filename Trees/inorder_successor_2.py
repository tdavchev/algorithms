class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

    def set_parent(self, data):
        self.parent = data

def find_minimum(node):
    while node.left != None:
        node = node.left

    return node

def find_susccessor(node):
    if node == None:
        return None

    if node.right != None:
        print(find_minimum(node.right).data)
        return

    while node.parent != None:
        if node.parent.left == node:
            print(node.parent.data)
            return

        node = node.parent
    if node.parent == None:
        print("None")

def inorder_successor(root, d):
    
    while root != None:
        if root.data > d:
            root = root.left
        elif root.data < d:
            root = root.right
        else:
            find_susccessor(root)
            break

def find_inorder_noparent(node, d):
    successor = None
    while node != None:
        if node.data < d:
            node = node.right
        elif node.data > d:
            successor = node
            node = node.left
        else:
            if root.right != None:
                successor = find_minimum(root.right)
            break

    return successor

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

root.set_parent(None)
ele1.set_parent(root)
ele2.set_parent(ele1)
ele3.set_parent(ele1)
ele4.set_parent(root)
ele5.set_parent(ele4)
ele6.set_parent(ele4)

inorder_successor(root, 350)
