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