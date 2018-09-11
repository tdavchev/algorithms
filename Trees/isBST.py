class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data

def checkBST(root):
    collection = set()
    bst = True
    node = root
    q = []
    while node is not None or len(q) > 0:
        if node != None:
            if node.data in collection or node.left.data > node.data or node.right.data < node.data:
                bst = False
                break
            collection.add(node.data)
            q.append(node)
            node = node.left
            continue
 
        node = q.pop().right
    print("I broke..")
    return bst

def isBST(root):
    if root == None:
        return False

    stack = []
    # ans = []
    prev = -99999

    while (len(stack) != 0 or root != None):
        if root != None:
            stack.append(root)
            root = root.left
            continue

        if prev > stack[-1].data:
            return False

        # ans.append(stack[-1])
        root = stack[-1].right
        prev = stack[-1].data
        stack.pop()

    # for i in range(1, len(ans)):
    #     if ans[i-1].data > ans[i].data:
    #         return False

    return True

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

print(checkBST(root))
    