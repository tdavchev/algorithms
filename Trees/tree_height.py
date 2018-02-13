class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data

def height(root):
    if root == None:
        return 0

    stack = []
    while root != None:
        stack.append(root)
        root = root.left

    count = len(stack)
    while len(stack) > 0:
        ele = stack.pop()
        if ele.right != None:
            ele = ele.right
            while ele != None:
                stack.append(ele)
                ele = ele.left

            if count < len(stack) + 1:
                count = len(stack) + 1

    print(count)

root = TreeNode(100)
ele1 = TreeNode(50)
ele2 = TreeNode(25)
ele3 = TreeNode(75)
ele4 = TreeNode(30)
ele5 = TreeNode(60)
ele6 = TreeNode(200)
ele7 = TreeNode(125)
ele8 = TreeNode(350)

root.set_left(ele1)
root.set_right(ele6)
ele1.set_left(ele2)
ele1.set_right(ele3)
ele2.set_right(ele4)
ele3.set_left(ele5)
ele6.set_left(ele7)
ele6.set_right(ele8)

height(root)
