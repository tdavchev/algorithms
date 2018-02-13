class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data

def populate_stack(root, stack):
    while root.right != None:
        stack.append(root.right)
        root = stack[-1]

    return stack


def find_nth_highest(root, n):
    if root == None:
        return None

    stack = []
    ans = []
    stack.append(root)
    stack = populate_stack(root, stack)

    while len(stack) > 0:
        ele = stack.pop()
        if ele.left != None:
            stack.append(ele.left)
            populate_stack(ele.left, stack)

        ans.append(ele)
        if len(ans) == n:
            return ele.data

    return -1

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

ans = find_nth_highest(root, 1)
print(ans)
    
    