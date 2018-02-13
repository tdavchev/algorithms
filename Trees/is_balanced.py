class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def getHeight(root):
    if root == None:
        return 0

    # print("tuk sam ", root.data)
    # print("----")

    return max(getHeight(root.left), getHeight(root.right)) + 1

def isBalanced(root):
    if root == None:
        return True

    heightDiff = getHeight(root.left) - getHeight(root.right)

    if abs(heightDiff) > 1:
        return False
    else:
        return True


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
# ele2.set_right(ele6)
# ele6.set_right(ele9)

print(isBalanced(root))
