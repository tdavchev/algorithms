# def is_bst(root):
import sys
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data


def is_bst_ebasi(root, min_value, max_value):
    if root == None:
        return True

    if root.data < min_value or root.data > max_value:
        return False

    return is_bst_ebasi(root.left, min_value, root.data) and is_bst_ebasi(root.right, root.data, max_value)

def is_bst2(root):
    return is_bst_ebasi(root, -sys.maxint - 1, sys.maxint)

def is_bst_rec(root, min_value, max_value):
    if root == None:
        return True

    if root.data < min_value or root.data > max_value:
        return False

    return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
    return is_bst_rec(root, -sys.maxsize, sys.maxsize)


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

print(is_bst(root))