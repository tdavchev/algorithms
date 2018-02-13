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

    temp = root.right
    root.right = root.left
    root.left = temp

    return root


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

ans = mirror_tree(root)
stck = []
while ans != None:
    stck.append(ans)
    ans = ans.left

while len(stck) > 0:
    ele = stck.pop()

    if ele.right != None:
        stck.append(ele.right)
        itm = ele.right
        while itm.left != None:
            stck.append(itm.left)
            itm = stck[-1]

    print(ele.data)

    