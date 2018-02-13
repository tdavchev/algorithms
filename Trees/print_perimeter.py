class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def left_side(root):
    while root.left != None:
        print(root.data)
        root = root.left

def leaf_nodes(root):
    stack = []
    while len(stack) != 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
            continue

        if stack[-1] != None:
            if stack[-1].left == None and stack[-1].right == None:
                print(stack[-1].data)
        
        root = stack.pop().right

def right_side(root):
    r_values = []
    root = root.right

    while root != None:
        curr_val = root.data

        if root.right != None:
            root = root.right
        elif root.left != None:
            root = root.left
        else:
            break

        r_values.append(curr_val)

    while len(r_values) != 0:
        print(r_values.pop())

root = TreeNode(1)
ele1 = TreeNode(2)
ele2 = TreeNode(3)
ele3 = TreeNode(4)
ele4 = TreeNode(5)
ele5 = TreeNode(6)
ele6 = TreeNode(7)
ele7 = TreeNode(8)
ele8 = TreeNode(9)
ele9 = TreeNode(10)

root.set_left(ele1)
root.set_right(ele2)
ele1.set_left(ele3)
ele1.set_right(ele4)
ele3.set_left(ele8)
ele4.set_right(ele7)
ele2.set_right(ele6)
ele6.set_right(ele9)

left_side(root)
leaf_nodes(root)
right_side(root)