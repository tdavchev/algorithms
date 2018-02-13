class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def iterative_inorder(root):
    if root == None:
        return None

    stack = []

    while len(stack) > 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
            continue

        print(stack[-1].data)
        root = stack.pop().right
            

def find_inorder_successor(root, node):
    if root == None:
        return None

    stack = []
    prev = False

    while len(stack) != 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
            continue
        
        if prev:
            print(stack[-1].data)
            return

        if stack[-1].data == node.data:
            prev = True
        
        root = stack.pop().right


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

find_inorder_successor(root, ele6)