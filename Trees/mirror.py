class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data


def mirror_tree(root):
    if root == None:
        return

    if root.left != None:
        mirror_tree(root.left)

    if root.right != None:
        mirror_tree(root.right)

    temp = root.left
    root.left = root.right
    root,right = temp


def mirror(root):
    mirrored = []
    mirr_root = TreeNode(root.data)
    mirrored.append(mirr_root)
    stack = []

    while len(stack) != 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
            if root != None:
                mirrored[-1].right = TreeNode(root.data)
                mirrored.append(mirrored[-1].right)

            continue

        root = stack.pop()
        item = [i for i in mirrored if i.data == root.data][0]
        root = root.right
        if root != None:
            item.left = TreeNode(root.data)
            mirrored.append(item.left)

    print("----------------")

    temp = mirrored[0]
    st = []
    while temp != None or len(st) != 0:
        if temp != None:
            st.append(temp)
            temp = temp.left
            continue

        print(st[-1].data)
        temp = st.pop().right

def copy(root):
    # print(root.data)
    mirrored = []
    mirr_root = TreeNode(root.data)
    mirrored.append(mirr_root)
    stack = []
    while (len(stack) != 0 or root != None):
        if root != None:
            stack.append(root)
            root = root.left
            if root != None:
                mirrored[-1].left = TreeNode(root.data)
                mirrored.append(mirrored[-1].left)
            continue

        print(stack[-1].data)
        root = stack.pop()
        itm = [i for i in mirrored if i.data == root.data][0]
        root = root.right
        if root != None:
            itm.right = TreeNode(root.data)
            mirrored.append(itm.right)
        


    print("----------------")

    for item in mirrored:
        print(item.data)

    print("----------------")

    temp = mirrored[0]
    st = []
    while temp != None or len(st) != 0:
        if temp != None:
            st.append(temp)
            temp = temp.left
            continue

        print(st[-1].data)
        temp = st.pop().right

root = TreeNode(20)
ele1 = TreeNode(50)
ele2 = TreeNode(200)
ele3 = TreeNode(75)
ele4 = TreeNode(25)
ele5 = TreeNode(300)

root.set_left(ele1)
root.set_right(ele2)
ele1.set_left(ele3)
ele1.set_right(ele4)
ele2.set_right(ele5)

mirror(root)
