def find_min_in_tree(root):
    while root.left != None:
        root = root.left

    return root

def inorder_successor(node):
    if node == None:
        return None

    if node.right != None:
        return find_min_in_tree(node.right)

    while node.parent != None:
        if node.parent.left == node:
            return node.parent

        node = node.parent

def find_successor(root, d):
    while root != None:
        if root.data < d:
            root = root.right
        elif curr.data > d:
            root = root.left
        else:
            # I can't just return the previous or the one above
            # if there was a right branch coming down d
            # then the successor might be below
            return inorder_successor(root)

    return None
            