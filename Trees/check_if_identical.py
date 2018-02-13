class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

def identical(root1, root2):
    # DFS
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None:
        return (root1.data == root2.data and
            identical(root1.left, root2.left) and
            identical(root1.right, root2.right))

    return False
