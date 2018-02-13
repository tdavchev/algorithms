def find_min(root):
    if root == None:
        return None

    while root != None:
        root = root.left

    return root

def inorder_successor(root, d):
    if root == None:
        return None

    successor = None

    while root != None:
        if root.data < d:
            root = root.right
        elif root.data > d:
            successor = root
            root = root.left
        else:
            if root.right != None:
                successor = find_min(root.right)
            break

    return successor